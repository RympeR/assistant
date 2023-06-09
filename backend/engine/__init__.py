from backend.engine.request.Command import CommandOBJ
from backend.engine.request.Request import RequestOBJ
from backend.engine.settings import MIDDLEWARE_CLASSES, MODULE_CLASSES
from backend.utils.import_utils import import_string


class Engine:
    modules = []
    middlewares = []

    def __init__(self):
        not_init_modules = []
        for middleware_class in MIDDLEWARE_CLASSES:
            middleware = import_string(middleware_class)
            self.middlewares.append(middleware)
        for module_class in MODULE_CLASSES:
            module = import_string(module_class)
            not_init_modules.append(module)
        self.module_initialization(not_init_modules)

    def module_initialization(self, modules):
        for module in modules:
            self.modules.append(module())

    def process_middlewares(self, request):
        request.middlewares = self.middlewares
        request.modules = self.modules
        for middleware in self.middlewares:
            Engine.process_middleware(request, middleware)
        return request

    def process_request(self, request):
        request = self.process_middlewares(request)
        for command in request.commands:
            for module in self.modules:
                if command.module == module.__class__.__name__:
                    return Engine.process(command.command, module, *request.args, **request.kwargs)
        # return Engine.process(request.command.command, request.command.module, *request.args, **request.kwargs)

    @staticmethod
    def process_middleware(request, middleware):
        init_middleware = middleware()
        if init_middleware:
            request = init_middleware(request)
        return request

    @staticmethod
    def process(command, module, *args, **kwargs):
        if getattr(module, command, None):
            return getattr(module, command)(*args, **kwargs)
        return None


if __name__ == '__main__':
    engine = Engine()
    command = CommandOBJ(
        command='coin',
        module='BaseCommands',
        _class='BaseCommands',
    )
    request = RequestOBJ(
        commands=[command],
        language='en',
    )
    print(engine.process_request(request))
