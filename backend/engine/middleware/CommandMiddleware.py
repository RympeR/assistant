class CommandMiddleware(object):
    def __call__(self, request):
        for command in request.commands:
            for module in request.modules:
                print(module)
                print(command.command)
                print(dir(module))
                if command.command in dir(module):
                    print(command.command)

                    command.module = module
                    command._class = module.__class__.__name__
        return request
