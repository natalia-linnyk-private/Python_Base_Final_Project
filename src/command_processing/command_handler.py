from src.enums.command_enums import ContactCommandEnum, NotesCommandEnum, GeneralCommandEnum, ExitCommandEnum
from src.data_models.address_book import AddressBook
from src.data_models.notes_manager import NotesManager
from src.command_processing import notes_command_processor, contact_command_processor

def get_all_command_list() -> list[str]:
    commands_list = []
    commands_list.extend([command.value for command in ContactCommandEnum])
    commands_list.extend([command.value for command in NotesCommandEnum])
    commands_list.extend([command.value for command in GeneralCommandEnum])
    commands_list.extend([command.value for command in ExitCommandEnum])
    return commands_list

def process_contact_command(command: str, args: list[str], book: AddressBook):
    match command:
        case ContactCommandEnum.ADD_CONTACT.value:
            return contact_command_processor.add_contact(args, book)
        case ContactCommandEnum.CHANGE_CONTACT.value:
            return contact_command_processor.update_contact(args, book)
        case ContactCommandEnum.SHOW_CONTACT_PHONE.value:
            return contact_command_processor.show_phones(args, book)
        case ContactCommandEnum.REMOVE_CONTACT_PHONE.value:
            return contact_command_processor.remove_phone(args, book)
        case ContactCommandEnum.ADD_CONTACT_EMAIL.value:
            return contact_command_processor.add_email(args, book)
        case ContactCommandEnum.SHOW_CONTACT_EMAIL.value:
            return contact_command_processor.show_emails(args, book)
        case ContactCommandEnum.REMOVE_CONTACT_EMAIL.value:
            return contact_command_processor.remove_email(args, book)
        case ContactCommandEnum.SHOW_ALL_CONTACTS.value:
            return contact_command_processor.show_all(book)
        case ContactCommandEnum.ADD_CONTACT_BIRTHDAY.value:
            return contact_command_processor.add_birthday(args, book)
        case ContactCommandEnum.SHOW_CONTACT_BIRTHDAY.value:
            return contact_command_processor.show_birthday(args, book)
        case ContactCommandEnum.UPCOMING_BIRTHDAYS.value:
            return contact_command_processor.birthdays(book, args)
        case ContactCommandEnum.REMOVE_CONTACT.value:
            return contact_command_processor.remove_contact(args, book)
        case ContactCommandEnum.FIND_CONTACT_BY_NAME.value:
            return contact_command_processor.find_contact_by_name(args, book)
        case ContactCommandEnum.FIND_CONTACT_BY_EMAIL.value:
            return contact_command_processor.find_contact_by_email(args, book)
        case ContactCommandEnum.ADD_CONTACT_ADDRESS.value:
            return contact_command_processor.add_address(args, book)
        case ContactCommandEnum.REMOVE_CONTACT_ADDRESS.value:
            return contact_command_processor.remove_address(args, book)

def process_notes_command(command: str, args: list[str], notes : NotesManager):
        match command:
            case NotesCommandEnum.ADD_NOTE.value:
                return notes_command_processor.add_note(args, notes)
            case NotesCommandEnum.EDIT_NOTE.value:
                return notes_command_processor.edit_note(args, notes)
            case NotesCommandEnum.DELETE_NOTE.value:
                return notes_command_processor.delete_note(args, notes)
            case NotesCommandEnum.LIST_NOTES.value:
                return notes_command_processor.list_notes(notes)
            case NotesCommandEnum.ADD_NOTE_TAG.value:
                return notes_command_processor.add_tag(args, notes)
            case NotesCommandEnum.REMOVE_NOTE_TAG.value:
                return notes_command_processor.remove_tag(args,notes)
            case NotesCommandEnum.SEARCH_NOTES.value:
                return notes_command_processor.search_notes_by_tag(args, notes)

def process_command(command: str, args: list[str], notes : NotesManager, book : AddressBook):
    if command in [member.value for member in ContactCommandEnum]:
        return process_contact_command(command, args, book)
    if command in [member.value for member in NotesCommandEnum]:
        return process_notes_command(command, args, notes)