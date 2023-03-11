from functools import wraps
from googletrans import Translator


def translate(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        translator = Translator()
        if isinstance(result, str):
            return translator.translate(result, dest=args[0].lang).text
        if isinstance(result, dict):
            return {
                key: translator.translate(value, dest=args[0].lang).text if isinstance(value, str) else value
                for key, value in result.items()
            }
        return result
    return wrapper


def serializer(additional_text: str = None, required_type: str = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            return {
                'return_value': func(*args),
                'type': required_type,
                'additional_text': additional_text,
            }
        return wrapper
    return decorator
