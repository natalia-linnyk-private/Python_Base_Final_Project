from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

import src.command_processing.command_processor as command_processor
from src.command_processing import notes_processor
from src.command_processing.command_parser import parse_input_data
from src.enums.command_enums import CommandEnum
from src.save_load_data.save_load_data import load_all_data, save_all_data
from rich.console import Console

console = Console()

def main():
    user_name = console.input("Enter your name >>> ")
    console.print(f"Welcome {user_name} to the assistant bot!", style="bold green")
    book, notes = load_all_data()
    print(command_processor.show_help_file())
    
    base_commands = [command.value for command in CommandEnum]
    exit_commands = list(CommandEnum.EXIT_COMMANDS.value)
    all_commands = base_commands + exit_commands
    command_completer = WordCompleter(all_commands, ignore_case=True)

    while True:
        try:
            user_data = input("[bold yellow]Enter the command >>>[/] ")
            command, *args = parse_input_data(user_data)

            if command.lower() == CommandEnum.HELP.value:
                print(command_processor.show_help_file())
                continue

            if command in CommandEnum.EXIT_COMMANDS.value:
                save_all_data(book, notes)
                console.print(f"Good bye {user_name}!", style="green")
                break

            match command:
                case CommandEnum.HELLO.value:
                    console.print(f"[purple]How can I help you, {user_name}?")
                case CommandEnum.ADD.value:
                    console.print(command_processor.add_contact(args, book))
                case CommandEnum.CHANGE.value:
                    console.print(command_processor.update_contact(args, book))
                case CommandEnum.SHOW_PHONE.value:
                    console.print(command_processor.show_phones(args, book))
                case CommandEnum.REMOVE_PHONE.value:
                    console.print(command_processor.remove_phone(args, book))
                case CommandEnum.ADD_EMAIL.value:
                    console.print(command_processor.add_email(args, book))
                case CommandEnum.SHOW_EMAIL.value:
                    console.print(command_processor.show_emails(args, book))
                case CommandEnum.REMOVE_EMAIL.value:
                    console.print(command_processor.remove_email(args, book))
                case CommandEnum.SHOW_ALL.value:
                    console.print(command_processor.show_all(book))
                case CommandEnum.ADD_BIRTHDAY.value:
                    console.print(command_processor.add_birthday(args, book))
                case CommandEnum.SHOW_BIRTHDAY.value:
                    console.print(command_processor.show_birthday(args, book))
                case CommandEnum.BIRTHDAYS.value:
                    console.print(command_processor.birthdays(book))

                case CommandEnum.ADD_NOTE.value:
                    console.print(notes_processor.add_note(args, notes))
                case CommandEnum.EDIT_NOTE.value:
                    console.print(notes_processor.edit_note(args, notes))
                case CommandEnum.DELETE_NOTE.value:
                    console.print(notes_processor.delete_note(args, notes))
                case CommandEnum.LIST_NOTES.value:
                    console.print(notes_processor.list_notes(notes))

                case CommandEnum.ADD_TAG.value:
                    console.print(notes_processor.add_tag(args,notes))
                case CommandEnum.REMOVE_TAG.value:
                    console.print(notes_processor.remove_tag(args,notes))
                case CommandEnum.SEARCH_NOTES.value:
                    console.print(notes_processor.search_notes(args, notes))

                case CommandEnum.REMOVE_CONTACT.value:
                    console.print(command_processor.remove_contact(args, book))
                case CommandEnum.FIND_CONTACT_BY_NAME.value:
                    console.print(command_processor.find_contact_by_name(args, book))
                case CommandEnum.FIND_CONTACT_BY_EMAIL.value:
                    console.print(command_processor.find_contact_by_email(args, book))
                case CommandEnum.ADD_ADDRESS.value:
                    console.print(command_processor.add_address(args, book))
                case CommandEnum.REMOVE_ADDRESS.value:
                    console.print(command_processor.remove_address(args, book))
                case _:
                    console.print("[red]Invalid command.[/]")
                    input_command = console.input("[yellow]Would you like to see all commands list? Y/N >>>[/] ").strip().lower()
                    if input_command == 'y':
                        console.print("[purple]" + command_processor.show_help_file())
        except Exception as error:
            console.print("[red]Error happened: ", error)


if __name__ == "__main__":
    main()