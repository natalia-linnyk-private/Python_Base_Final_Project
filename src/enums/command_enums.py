from enum import Enum

class ContactCommandEnum(Enum):
    ADD_CONTACT = "add"
    CHANGE_CONTACT = "change"
    REMOVE_CONTACT = "remove"
    SHOW_ALL_CONTACTS = "all"
    FIND_CONTACT_BY_NAME = "find-by-name"
    FIND_CONTACT_BY_EMAIL = "find-by-email"
    SHOW_CONTACT_PHONE = "phone"
    REMOVE_CONTACT_PHONE = "remove-phone"
    ADD_CONTACT_EMAIL = "add-email"
    SHOW_CONTACT_EMAIL = "email"
    REMOVE_CONTACT_EMAIL = "remove-email"
    ADD_CONTACT_BIRTHDAY = "add-birthday"
    SHOW_CONTACT_BIRTHDAY = "show-birthday"
    UPCOMING_BIRTHDAYS = "birthdays"
    ADD_CONTACT_ADDRESS = "add-address"
    REMOVE_CONTACT_ADDRESS = "remove-address"

class NotesCommandEnum(Enum):
    ADD_NOTE = "add-note"
    EDIT_NOTE = "edit-note"
    DELETE_NOTE = "remove-note"
    LIST_NOTES = "all-notes"
    ADD_NOTE_TAG = "add-tag"
    REMOVE_NOTE_TAG = "remove-tag"
    SEARCH_NOTES = "find-notes"

class GeneralCommandEnum(Enum):
    HELLO = "hello"
    HELP = "help"

class ExitCommandEnum(Enum):
    EXIT = "exit"
    CLOSE = "close"