class Command:
    def __init__(self, command, args, kwargs):
        self.command = command
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f'Command: {self.command}, args: {self.args}, kwargs: {self.kwargs}'
