from src.data_models.record_fields import Phone
from src.error_handling.error_handler import input_error
from src.data_models.address_book import AddressBook
from src.data_models.address_book_record import Record, Email
from src.constants import messages
from src.helpers import table_helper

COUNT_DAYS_UPCOMING_BIRTHDAYS = 7
HELP_FILE_PATH = "help.txt"

def is_record_found(record: Record) -> bool:
    if record is None:
        raise KeyError(messages.CONTACT_NOT_FOUND_MESSAGE)
    return True

def show_help_file():
    try:
        with open(HELP_FILE_PATH, mode="r", encoding="UTF-8") as file_object:
            help_text = file_object.read()
        return help_text
    except FileNotFoundError:
        return messages.FILE_NOT_FOUND_ERROR_MESSAGE

@input_error
def add_contact(args, book: AddressBook):
    name = args[0]
    phone = args[1]
    book_record = book.find_by_name(name)
    message = messages.CONTACT_UPDATED_MESSAGE
    if book_record is None:
        book_record = Record(name)
        book.add_record(book_record)
        message = messages.CONTACT_ADDED_MESSAGE
    if phone:
        book_record.add_phone(phone)
    return message

@input_error
def update_contact(args, book: AddressBook):
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    message = book_record.edit_phone(old_phone, new_phone)
    return message

@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    phone_numbers = ', '.join(str(phone) for phone in book_record.phones)
    return phone_numbers

@input_error
def remove_phone(args, book):
    name = args[0]
    phone = args[1]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    return book_record.remove_phone(Phone(phone))

@input_error
def add_email(args, book: AddressBook):
    name = args[0]
    email = args[1]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    book_record.add_email(Email(email))
    return messages.EMAIL_ADDED_MESSAGE

@input_error
def show_emails(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    if len(book_record.emails) > 0:
        emails = ', '.join(str(email) for email in book_record.emails)
        return emails
    else:
        return messages.EMAILS_LIST_IS_EMPTY_MESSAGE

@input_error
def remove_email(args, book: AddressBook):
    name = args[0]
    email = args[1]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    return book_record.remove_email(Email(email))

@input_error
def show_all(book: AddressBook):
    if not book.data:
        raise ValueError(messages.BOOK_IS_EMPTY)
    else:
        return table_helper.create_address_book_table(book)

@input_error
def add_birthday(args, book: AddressBook):
    name = args[0]
    birthday_str = args[1]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    message = book_record.add_birthday(birthday_str)
    return message

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    if book_record.birthday is None:
        raise ValueError(messages.BIRTHDAY_NOT_ADDED_MESSAGE)
    
    return messages.SHOW_BIRTHDAY_MESSAGE.format(name, book_record.birthday)

@input_error
def birthdays(book: AddressBook, args):
    if len(args) > 0:
        upcoming_birthdays = book.get_upcoming_birthdays(int(args[0]))
    else:
        upcoming_birthdays = book.get_upcoming_birthdays(COUNT_DAYS_UPCOMING_BIRTHDAYS)
    if not upcoming_birthdays:
        return messages.NO_UPCOMMING_BIRTHDAY_FOUND_MESSAGE
    return table_helper.create_birthday_table(upcoming_birthdays)

@input_error
def remove_contact(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    book.delete_record(name)
    return messages.CONTACT_REMOVED_MESSAGE

@input_error
def find_contact_by_name(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    return table_helper.create_find_contact_table([book_record])

@input_error
def find_contact_by_email(args, book: AddressBook):
    email = args[0]
    email_obj = Email(email)
    book_records = book.find_by_email(email_obj)
    if len(book_records) == 0:
        raise KeyError(messages.CONTACT_NOT_FOUND_BY_EMAIL_MESSAGE)
    return table_helper.create_find_contact_table(list(book_records))

@input_error
def add_address(args, book: AddressBook):
    name = args[0]
    address = args[1::]
    address_str = ' '.join(address)
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    result_message = messages.ADDRESS_ADDED_MESSAGE if book_record.address is None else messages.ADDRESS_UPDATED_MESSAGE
    book_record.add_address(address_str)
    return result_message

@input_error
def remove_address(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    if book_record.address is None:
        raise ValueError(messages.ADDRESS_DOES_NOT_EXISTS_MESSAGE)
    book_record.address = None
    return messages.ADDRESS_REMOVED_MESSAGE
