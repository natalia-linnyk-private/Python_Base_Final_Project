# Messages for main.py
ASK_USER_NAME_MESSAGE = "Enter your name >>> "
WELCOME_MESSAGE = "Welcome to the assistant bot,"
ASK_COMMAND_MESSAGE = "Enter the command >>> "
INVALID_COMMAND_MESSAGE = "Invalid command.[/]"
QUESTION_HELP_FILE_MESSAGE = "Would you like to see all commands list? Y/N >>>[/] "
GOOD_BYE_MESSAGE = "Good bye, "
HELLO_COMMAND_MESSAGE = "How can I help you, "
UNEXPECTED_ERROR_MESSAGE = "Error happened: "

# Messages from error handler
KEY_ERROR_MESSAGE = "Error accessing contacts"
VALUE_ERROR_MESSAGE = "Wrong format of input data"
INDEX_ERROR_MESSAGE = "Not enough count of arguments"
FILE_NOT_FOUND_ERROR_MESSAGE = "Help file not found"

#Messages from notes command handler
REQUIRED_TITLE_MESSAGE = "Title is required."
SUCCESS_NOTE_CREATION_MESSAGE = "Created note: "

#Messages from contact command processor
CONTACT_NOT_FOUND_MESSAGE = "Contact not found in the book."
CONTACT_ADDED_MESSAGE = "Contact added"
CONTACT_UPDATED_MESSAGE = "Contact updated"
EMAIL_ADDED_MESSAGE = "Email was added successfully"
BOOK_IS_EMPTY = "Address book is empty"
BIRTHDAY_NOT_ADDED_MESSAGE = "Birthday is not set for this contact yet."
NO_UPCOMMING_BIRTHDAY_FOUND_MESSAGE = "No upcoming birthdays found."
ADDRESS_ADDED_MESSAGE = "Address added."
ADDRESS_UPDATED_MESSAGE = "Address updated."
ADDRESS_DOES_NOT_EXISTS_MESSAGE = "Address is not set for this contact."
ADDRESS_REMOVED_MESSAGE = "Address was removed."
CONTACT_NOT_FOUND_BY_EMAIL_MESSAGE = "No contacts found with the provided email."
EMAILS_LIST_IS_EMPTY_MESSAGE = "List of emails for this contact is empty."
CONTACT_REMOVED_MESSAGE = "Contact removed."
SHOW_BIRTHDAY_MESSAGE = "{0}'s birthday is on {1}"

#Validation errors
INVALID_EMAIL_ADDRESS_MESSAGE = "Invalid format of email address."
INVALID_DATE_FORMAT = "Invalid date format. Date format should be DD.MM.YYYY"
INVALID_BIRTHDAY_FORMAT = "Birthday date must be a string"
BIRTHDAY_IN_FUTURE = "Birthday date cannot be in the future"
EMPTY_NAME_MESSAGE = "Name cannot be empty"
INVALID_PHONE_NUMBER = "Phone number must be 10 digits"

# Messages from record fields
PHONE_WAS_ADDED_MESSAGE = "Phone {0} added to {1}"
PHONE_NUMBER_EXISTS_MESSAGE = "Phone {0} already exists for {1}"
PHONE_NUMBER_UPDATED_MESSAGE = "Phone {0} changed to {1} for {2}"
PHONE_NUMBER_NOT_FOUND = "Phone {0} not found for {1}"
PHONE_NUMBER_REMOVED_MESSAGE = "Phone {0} removed from {1}"
BIRTHDAY_ADDED_MESSAGE = "Birthday {0} added to {1}."
EMAIL_EXISTS_MESSAGE = "Email {0} already exists for {1}"
EMAIL_IS_NOT_SET_MESSAGE = "Email {0} is not set for this contact."
EMPTY_ADDRESS_MESSAGE = "Address cannot be empty"

#Messages from address book class
INVALID_DATA_MESSAGE = "Only Record objects can be added to address book"
SUCCESS_ADDING_RECORD_MESSAGE = "Record for {0} added to address book."
SUCCESS_DELETING_RECORD_MESSAGE = "Record for {0} deleted from address book."
RECORD_NOT_FOUND_MESSAGE = "Record for {0} not found in address book."

#Messages related to notes logic
NOTES_EMPTY_MESSAGE = "Notes book is empty"
SUCCESS_DELETING_NOTE_MESSAGE = "Deleted note {0}"
NOTE_NOT_FOUND_MESSAGE = "Note was not found."
NO_CHAGES_WAS_MADE_MESSAGE = "No changes made."
SUCCESS_UPDATING_NOTE_MESSAGE = "Updated note '{0}' ({1})"
NOTE_NOT_FOUND_MESSAGE = "Note not found in the book."
MATCHING_NOTES_NOT_FOUND_MESSAGE = "Matching Notes were not found"
SUCCESS_TAG_ADDED_MESSAGE = "Tag was added successfully"
SUCCESS_TAG_REMOVED_MESSAGE = "Tag was removed successfully"
TAG_NOT_FOUND_MESSAGE = "No such tag for this note found"
NO_SUCH_SORT_BY_PARAM_MESSAGE = "No such sort param available"