from typing import Union, List
from .Command import Command


class Request:
    command: Union[Command, None] = None
    args: List[str] = None

    def __init__(self):
        ...
