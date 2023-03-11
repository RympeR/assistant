from dataclasses import dataclass


@dataclass
class Command:
    command: str = None
    module: str = None
    _class: str = None
    args: list = None
    kwargs: dict = None

    def __str__(self):
        return f'Command: {self.command}, args: {self.args}, kwargs: {self.kwargs}'
