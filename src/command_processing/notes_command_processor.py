from rich.table import Table

from src.data_models.notes_manager import NotesManager, Note
from src.error_handling.error_handler import input_error
from src.constants import messages
from src.helpers import table_helper
from src.enums.notes_enum import SortNotesParamEnum

@input_error
def add_note(args, notes: NotesManager):
    title = " ".join(args)
    if len(title) == 0:
        raise ValueError(messages.REQUIRED_TITLE_MESSAGE)
    note_id = notes.new(title)
    return f"{messages.SUCCESS_NOTE_CREATION_MESSAGE}{note_id}"

@input_error
def edit_note(args, notes: NotesManager):
    note_id = args[0]
    return notes.edit_in_editor(int(note_id))

@input_error
def delete_note(args, notes: NotesManager):
    note_id = args[0]
    return notes.delete(int(note_id))

@input_error
def list_notes(notes: NotesManager):
    return as_table(notes.notes)

@input_error
def show_note_content(args, notes: NotesManager):
    note_id = args[0]
    note = notes.get(int(note_id))
    if not note:
        raise KeyError(messages.NOTE_NOT_FOUND_MESSAGE)
    return note.content

@input_error
def add_tag(args, notes: NotesManager):
    note_id = args[0]
    tag = args[1]
    note = notes.get(int(note_id))
    if not note:
        raise KeyError(messages.NOTE_NOT_FOUND_MESSAGE)
    note.add_tag(tag)
    return messages.SUCCESS_TAG_ADDED_MESSAGE

@input_error
def remove_tag(args, notes: NotesManager):
    note_id = args[0]
    tag = args[1]
    note = notes.get(int(note_id))
    if not note:
        raise KeyError(messages.NOTE_NOT_FOUND_MESSAGE)
    note.remove_tag(tag)
    return messages.SUCCESS_TAG_REMOVED_MESSAGE

@input_error
def search_notes_by_tag(args, notes: NotesManager):
    tag = args[0]
    if len(args) > 1:
        sort_by = args[1]
        if sort_by not in [member.value for member in SortNotesParamEnum]:
            raise ValueError(messages.NO_SUCH_SORT_BY_PARAM_MESSAGE)
        found_notes = dict(notes.search_by_tag(tag, sort_by))
    else:
        found_notes = dict(notes.search_by_tag(tag))
    if len(found_notes) == 0:
        raise KeyError(messages.MATCHING_NOTES_NOT_FOUND_MESSAGE)
    return as_table(found_notes)

def as_table(notes: dict[int, Note] | None) -> Table:
    if len(notes) == 0:
        raise ValueError(messages.NOTES_EMPTY_MESSAGE)
    else:
        return table_helper.create_table_notes(notes)
