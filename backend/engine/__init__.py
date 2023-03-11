from backend.engine.settings import MIDDLEWARE_CLASSES, MODULE_CLASSES
from backend.utils.import_utils import import_string


class Engine:
    def __init__(self):
        self.middlewares = []
        self.modules = []
        for middleware_class in MIDDLEWARE_CLASSES:
            middleware = import_string(middleware_class)
            print(middleware)
            self.middlewares.append(middleware)
        for module_class in MODULE_CLASSES:
            module = import_string(module_class)
            print(module)
            self.modules.append(module)
        print(self.middlewares)

    def process(self, command, *args, **kwargs):
        for module in self.modules:
            if getattr(module, command, None):
                return getattr(module, command)(*args, **kwargs)
        return None


if __name__ == '__main__':
    engine = Engine()
    engine.process('get_temperature', 'Moscow')