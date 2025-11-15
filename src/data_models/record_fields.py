import re
from datetime import datetime

from rich.table import Table
from rich.text import Text
from src.constants import messages, style_consts

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
MAX_LEN_PHONE_NUMBER = 10

class Field:
    def __init__(self, value):
        self.value = value

    def __rich__(self):
        return Text(str(self.value), style="medium_spring_green")

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

class ListField(Field):
    def __rich__(self):
        sub = Table(show_header=False, box=None, padding=0, style=style_consts.PROGRESS_BAR_FINISH_STYLE)
        for item in self.value:
            sub.add_row(item)
        return sub

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError(messages.EMPTY_NAME_MESSAGE)
        super().__init__(value)

    def __rich__(self):
        return Text(self.value, style=style_consts.SUCCESS_RESPONSE_TEXT_COLOR)


class Phone(Field):
    def __init__(self, value):
        if not self.is_phone_number_valid(value):
            raise ValueError(messages.INVALID_PHONE_NUMBER)
        super().__init__(value)
    
    def is_phone_number_valid(self, phone_number):
        return phone_number.isdigit() and len(phone_number) == MAX_LEN_PHONE_NUMBER
        
    def __rich__(self):
        return Text(self.value, style="magenta3")

class Email(Field):
    def __init__(self, email: str):
        self.is_email_valid(email)
        super().__init__(email)

    def is_email_valid(self, email: str):
        if re.match(EMAIL_REGEX, email) is None:
            raise ValueError(messages.INVALID_EMAIL_ADDRESS_MESSAGE)

    def update(self, email):
        self.is_email_valid(email)
        self.value = email

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = self.parse_birthday(value)
        except ValueError:
            raise ValueError(messages.INVALID_DATE_FORMAT)
        super().__init__(self.value)
        
    def parse_birthday(self, value):
        if not isinstance(value, str):
            raise ValueError(messages.INVALID_BIRTHDAY_FORMAT)
        
        birthday_date = datetime.strptime(value, "%d.%m.%Y").date()

        if birthday_date > datetime.now().date():
            raise ValueError(messages.BIRTHDAY_IN_FUTURE)

        return birthday_date
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

    def age(self):
        today = datetime.today()
        age = today.year - self.value.year
        if (today.month, today.day) < (self.value.month, self.value.day):
            age -= 1
        return age
