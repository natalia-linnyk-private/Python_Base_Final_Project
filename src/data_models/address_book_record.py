from typing import List

from src.data_models.record_fields import Name, Phone, Email
from src.data_models.record_fields import Birthday
from src.constants import messages

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.emails: List[Email] = []
        self.birthday: Birthday|None = None
        self.address: str|None = None

    def add_phone(self, phone_number):
        if Phone(phone_number) not in self.phones:
            self.phones.append(Phone(phone_number))
            return messages.PHONE_WAS_ADDED_MESSAGE.format(phone_number, self.name)
        else:
            raise ValueError(messages.PHONE_NUMBER_EXISTS_MESSAGE.format(phone_number, self.name))
    
    def edit_phone(self, old_phone_number, new_phone_number):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone_number:
                self.phones[index] = Phone(new_phone_number)
                return messages.PHONE_NUMBER_UPDATED_MESSAGE.format(old_phone_number, new_phone_number, self.name)
        
        raise ValueError(messages.PHONE_NUMBER_NOT_FOUND.format(old_phone_number, self.name))
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone.value
        
        raise ValueError(messages.PHONE_NUMBER_NOT_FOUND.format(phone_number, self.name))
    
    def remove_phone(self, phone: Phone):
        if not phone in self.phones:
            raise ValueError(messages.PHONE_NUMBER_NOT_FOUND.format(phone.value, self.name))
        self.phones.remove(phone)
        return messages.PHONE_NUMBER_REMOVED_MESSAGE.format(phone, self.name)

    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)
        return messages.BIRTHDAY_ADDED_MESSAGE.format(birthday_str, self.name)

    def add_email(self, email: Email):
        if email in self.emails:
            raise ValueError(messages.EMAIL_EXISTS_MESSAGE.format(email, self.name))
        self.emails.append(email)

    def remove_email(self, email: Email):
        if not email in self.emails:
            raise ValueError(messages.EMAIL_IS_NOT_SET_MESSAGE.format(email))
        self.emails.remove(email)
        return "Email removed."

    def add_address(self, address: str):
        if not address:
            raise ValueError(messages.EMPTY_ADDRESS_MESSAGE)
        self.address = address

    def __str__(self):
        age = f"(age: {self.birthday.age()})" if self.birthday else ""
        return (f"{self.name}:"
                f"\n\tphones: {'; '.join(p.value for p in self.phones)}"
                f"\n\temails: {'; '.join(e.value for e in self.emails)}"
                f"\n\taddress: {self.address if self.address else 'N/A'}"
                f"\n\tbirthday: {self.birthday if self.birthday else 'N/A'}\t{age}")
