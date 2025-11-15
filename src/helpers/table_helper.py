from rich.table import Table
from src.constants import table_columns
from src.data_models.record_fields import ListField
from src.data_models.address_book import AddressBook
from src.constants import style_consts
from src.data_models.address_book_record import Record
from src.data_models.notes_manager import Note

def create_table_header(column_names : list, table_title: str) -> Table:
    table = Table(title=table_title, show_lines=True, show_header=True)
    table = Table(
        show_header=True,
        show_lines=True,
        header_style=style_consts.TABLE_HEADER_STYLE,
        border_style=style_consts.TABLE_BORDER_STYLE,
        row_styles=style_consts.TABLE_ROW_STYLES,
        title=table_title,
        title_style=style_consts.TABLE_TITLE_STYLE)

    for column in column_names:
        table.add_column(column, style_consts.TABLE_ROW_STYLES)
    return table

def add_single_book_record(record : Record, table : Table):
    table.add_row(record.name,
                      ListField(record.emails),
                      ListField(record.phones),
                      record.birthday,
                      record.address)

def create_address_book_table(book: AddressBook) -> Table:
    table = create_table_header(table_columns.ADDRESS_BOOK_COLUMNS, table_columns.ADDRESS_BOOK_HEADER)
    for record in book.values():
        add_single_book_record(record, table)
    return table

def create_birthday_table(upcomming_birthdays: dict) -> Table:
    table = create_table_header(table_columns.UPCOMMING_BIRTHDAY_COLUMNS, table_columns.UPCOMMING_BIRTHDAY_HEADER)
    for record in upcomming_birthdays:
        table.add_row(record["name"],
                      record["congratulation_date"])
    return table

def create_find_contact_table(records : list[Record]) -> Table:
    table = create_table_header(table_columns.ADDRESS_BOOK_COLUMNS, table_columns.SINGLE_CONTACT_TABLE_HEADER)
    for record in records:
        add_single_book_record(record, table)
    return table

def create_table_notes(notes: dict[int, Note] | None) -> Table:
    table = create_table_header(table_columns.NOTES_TABLE_COLUMNS, table_columns.NOTES_TABLE_HEADER)
    for id, note in notes.items():
            table.add_row(
                str(id),
                note,
                ListField(note.tags),
                note.created_at,
                note.updated_at,
            )
    return table