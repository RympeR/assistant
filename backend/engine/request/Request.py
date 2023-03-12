from typing import Union, List
from backend.engine.request.Command import CommandOBJ
from dataclasses import dataclass
from backend.engine.settings import set_language


@dataclass
class RequestOBJ:
    commands: Union[List[CommandOBJ], None] = None
    language: Union[str, None] = None
    args: Union[List[str], None] = None
    kwargs: Union[dict, None] = None
    middlewares: Union[list, None] = None
    modules: Union[list, None] = None

    def __init__(self, commands: Union[List[CommandOBJ], None] = None, language: Union[str, None] = None,
                 middlewares: Union[list, None] = None, modules: Union[list, None] = None,
                 *args: Union[List[str], None], **kwargs: Union[dict, None]):
        self.commands = commands
        self.args = args
        self.kwargs = kwargs
        self.middlewares = middlewares
        self.modules = modules
        set_language(language)

    def __str__(self):
        return f'Request: {self.commands}, args: {self.args}, kwargs: {self.kwargs}'

    def __repr__(self):
        return f'Request: {self.commands}, args: {self.args}, kwargs: {self.kwargs}'

    def __bool__(self):
        return bool(self.commands)


if __name__ == '__main__':
    print(RequestOBJ())
