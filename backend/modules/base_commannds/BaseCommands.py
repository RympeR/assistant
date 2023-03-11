from random import choice
import pyjokes
from backend.utils.utils import translate, serializer
from backend.engine.settings import USER_LANGUAGE


class BaseCommands:
    """
    Base commands for assistant
        methods:
            coin() - return heads or tails
            joke() - return joke
            translate(text, lang) - translate text to lang
                args:
                    text: str - text to translate
                    lang: str - language to translate
    """
    coin_choices = ['heads', 'tails']

    def __init__(self):
        self.lang = USER_LANGUAGE

    @translate
    @serializer("coin")
    def coin(self):
        return choice(BaseCommands.coin_choices)

    @translate
    @serializer("joke")
    def joke(self):
        return pyjokes.get_joke()

    @translate
    @serializer("translate")
    def translate(self, text: str):
        return text
