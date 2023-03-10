from functools import wraps
from googletrans import Translator


def translate(func):
    @wraps(func)
    def wrapper(*args):
        translator = Translator()
        return translator.translate(func(*args), dest=args[0].lang).text
    return wrapper
