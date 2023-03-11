from typing import Union, List
from backend.engine.request.Command import Command
from dataclasses import dataclass


@dataclass
class Request:
    command: Union[Command, None] = None
    args: Union[List[str], None] = None
    kwargs: Union[dict, None] = None

    def __str__(self):
        return f'Request: {self.command}, args: {self.args}, kwargs: {self.kwargs}'

    def __repr__(self):
        return f'Request: {self.command}, args: {self.args}, kwargs: {self.kwargs}'

    def __bool__(self):
        return bool(self.command)


if __name__ == '__main__':
    print(Request())
