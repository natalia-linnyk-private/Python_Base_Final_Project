from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.completion import WordCompleter
from rich.text import Text
from rich.console import Console
from prompt_toolkit.styles import Style

from src.constants import style_consts, messages
import src.command_processing.contact_command_processor as contact_command_processor
from src.command_processing.command_parser import parse_input_data
from src.enums.command_enums import GeneralCommandEnum, ExitCommandEnum
from src.save_load_data.save_load_data import load_all_data, save_all_data
from src.command_processing.command_handler import get_all_command_list, process_command
from src.helpers import first_word_completer

console = Console()

def main():
    try:
        prompt_text = Text(messages.ASK_USER_NAME_MESSAGE, style=style_consts.WELCOME_TEXT_STYLE)
        user_name = console.input(prompt_text)
        console.print(f"[{style_consts.WELCOME_TEXT_STYLE}]{messages.WELCOME_MESSAGE} {user_name}[/]")
        book, notes = load_all_data()
        console.print(style_consts.HELP_FILE_TEXT_COLOR + contact_command_processor.show_help_file())
        all_command_list = get_all_command_list()
        command_completer = WordCompleter(all_command_list, ignore_case=True)
        filter_completer = first_word_completer.FirstWordFilterCompleter(command_completer)
        session = PromptSession(style=Style.from_dict(style_consts.AUTO_COMPLETE_STYLE))

        while True:
            try:
                user_data = session.prompt(HTML(f"<{style_consts.PROMPT_COLOR}>{messages.ASK_COMMAND_MESSAGE}</{style_consts.PROMPT_COLOR}>"), completer=filter_completer, complete_while_typing=True)
                command, *args = parse_input_data(user_data)

                if not command in all_command_list:
                    console.print(f"{style_consts.ERROR_TEXT_COLOR}{messages.INVALID_COMMAND_MESSAGE}")
                    input_command = console.input(f"{style_consts.ASK_QUESTION_TEXT_COLOR}{messages.QUESTION_HELP_FILE_MESSAGE}").strip().lower()
                    if input_command == 'y':
                        console.print(style_consts.HELP_FILE_TEXT_COLOR + contact_command_processor.show_help_file())
                    continue

                if command in [command.value for command in ExitCommandEnum]:
                    save_all_data(book, notes)
                    prompt_text = Text(f"{messages.GOOD_BYE_MESSAGE}{user_name}!", style=style_consts.WELCOME_TEXT_STYLE)
                    console.print(prompt_text)
                    break

                match command:
                    case GeneralCommandEnum.HELLO.value:
                        console.print(f"{style_consts.HELP_FILE_TEXT_COLOR}{messages.HELLO_COMMAND_MESSAGE}{user_name}?")
                    case GeneralCommandEnum.HELP.value:
                        console.print(style_consts.HELP_FILE_TEXT_COLOR + contact_command_processor.show_help_file())

                console.print(process_command(command, args, notes, book))
            except Exception as error:
                console.print(f"{style_consts.ERROR_TEXT_COLOR}{messages.UNEXPECTED_ERROR_MESSAGE}", error)
    except:
        console.print(f"{style_consts.ERROR_TEXT_COLOR}{messages.UNEXPECTED_ERROR_MESSAGE}", error)

if __name__ == "__main__":
    main()