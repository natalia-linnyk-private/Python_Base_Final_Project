from rich.text import Text


def input_error(func):

    def red(error: str) -> Text:
        return Text(error, style="bold red")

    def green(success) -> Text:
        if isinstance(success, str):
            return Text(success, style="green")
        else:
            return success

    def inner(*args, **kwargs):
        try:
            return green(func(*args, **kwargs))
        except KeyError as error:
            return red(error.args[0] if error.args else "Error accessing contacts")
        except ValueError as error:
            return red(error.args[0] if error.args else "Wrong format of input data")
        except IndexError:
            return red("Not enough count of arguments")
        except FileNotFoundError as error:
            return red(error.args[0] if error.args else "Help file not found")
    return inner