from dataclasses import dataclass
from typing import Union


@dataclass
class CommandOBJ:
    command: Union[str, None] = None
    module: Union[str, None] = None
    _class: Union[str, None] = None
    args: Union[list, None] = None
    kwargs: Union[dict, None] = None

    def __str__(self):
        return f'Command: {self.command}, args: {self.args}, kwargs: {self.kwargs}'
