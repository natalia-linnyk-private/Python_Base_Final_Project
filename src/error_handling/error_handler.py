from rich.text import Text
from rich.table import Table
from src.constants import style_consts, messages

def input_error(func):

    def red(error: str) -> Text:
        return Text(error, style=style_consts.CUSTOM_ERROR_TEXT_COLOR)

    def green(success):
        if isinstance(success, str):
            return Text(success, style=style_consts.SUCCESS_RESPONSE_TEXT_COLOR)
        else:
            return success

    def inner(*args, **kwargs):
        try:
            return green(func(*args, **kwargs))
        except KeyError as error:
            return red(error.args[0] if error.args else messages.KEY_ERROR_MESSAGE)
        except ValueError as error:
            return red(error.args[0] if error.args else messages.VALUE_ERROR_MESSAGE)
        except IndexError as error:
            return red(messages.INDEX_ERROR_MESSAGE)
        except FileNotFoundError as error:
            return red(error.args[0] if error.args else messages.FILE_NOT_FOUND_ERROR_MESSAGE)
    return inner