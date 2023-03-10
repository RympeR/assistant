from random import choice
import pyjokes
from googletrans import Translator
from backend.utils.utils import translate

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
    translator = Translator()
    lang = 'ru'

    def __init__(self, lang: str = 'ru'):
        self.lang = lang

    @translate
    def coin(self):
        return choice(BaseCommands.coin_choices)

    @translate
    def joke(self):
        return pyjokes.get_joke()

    @translate
    def translate(self, text: str):
        return text


if __name__ == '__main__':
    base_command = BaseCommands('fr')
    print(base_command.coin())
    print(base_command.joke())
    print(base_command.translate('Привет'))