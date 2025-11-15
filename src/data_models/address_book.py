from collections import UserDict
from src.data_models.address_book_record import Record
from datetime import datetime
from src.data_models.record_fields import Email
from src.constants import messages

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}
    
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError(messages.INVALID_DATA_MESSAGE)
        
        self.data[record.name.value] = record
        return messages.SUCCESS_ADDING_RECORD_MESSAGE.format(record.name)
    
    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            return messages.SUCCESS_DELETING_RECORD_MESSAGE.format(name)
        else:
            raise ValueError(messages.RECORD_NOT_FOUND_MESSAGE.format(name))
    
    def get_upcoming_birthdays(self, days):
        upcoming_birthdays = []
        todays_date = datetime.now().date()
        
        for record in self.data.values():
            if record.birthday is not None:
                next_birthday_date = datetime(year=todays_date.year,
                                              month=record.birthday.value.month,
                                              day=record.birthday.value.day).date()
        
                if next_birthday_date < todays_date:
                    next_birthday_date = datetime(year=todays_date.year + 1,
                                                  month=record.birthday.value.month,
                                                  day=record.birthday.value.day).date()

                difference = next_birthday_date - todays_date
                if difference.days <= days:
                    user_congrats = {"name": record.name.value, "congratulation_date": next_birthday_date.strftime("%d.%m.%Y")}
                    upcoming_birthdays.append(user_congrats)
        
        return upcoming_birthdays

    def find_by_name(self, name) -> Record:
        return self.data.get(name, None)

    def find_by_email(self, email: Email) -> list[Record]:
       return [record for record in self.data.values() if email in record.emails]