import datetime
from prompt_toolkit import Application
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import TextArea, Label
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit
from src.constants import messages
from src.enums.notes_enum import SortNotesParamEnum

from rich.text import Text

from src.data_models.record_fields import Field

class DateField(Field):
    def __init__(self, date):
        super().__init__(date)

    def __str__(self):
        return self.value.strftime("%Y-%m-%d %H:%M")

    def __rich__(self):
        return Text(self.__str__(), style="dodger_blue2")

class Note(Field):
    def __init__(self, title):
        super().__init__(title)
        self.content = ""
        self.created_at = DateField(datetime.datetime.now())
        self.updated_at = self.created_at
        self.tags = set()

    def edit(self, new_content):
        self.content = new_content
        self.updated_at = DateField(datetime.datetime.now())

    def add_tag(self, tag: str):
        self.tags.add(tag)

    def remove_tag(self, tag : str):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            raise ValueError(messages.TAG_NOT_FOUND_MESSAGE)

class NotesManager():
    def __init__(self):
        super().__init__()
        self.notes = {}
        self.note_counter = 0 if len(self.notes) == 0 else max(self.notes.keys()) + 1

    def new(self, title):
        note_id = self.note_counter
        self.note_counter += 1
        note = Note(title)
        self.notes[note_id] = note
        return note_id

    def get(self, key, default=None) -> Note:
        return self.notes.get(key, default)

    def search_by_tag(self, tag: str, sort_by=None):
        notes_with_tag = []
        for nid, note in self.notes.items():
            if tag.lower() in note.tags:
                notes_with_tag.append((nid, note))
        
        if sort_by:
            match sort_by:
                case SortNotesParamEnum.SORT_BY_ID.value:
                    notes_with_tag.sort(key=lambda x: x[0], reverse=True)
                case SortNotesParamEnum.SORT_BY_TITLE.value:
                    notes_with_tag.sort(key=lambda x: Note(x[1]).value, reverse=True)
                case SortNotesParamEnum.SORT_BY_CREATED_DATE.value:
                    notes_with_tag.sort(key=lambda x: Note(x[1]).created_at, reverse=True)
                case SortNotesParamEnum.SORT_BY_UPDATED_DATE.value:
                    notes_with_tag.sort(key=lambda x: Note(x[1]).updated_at, reverse=True)
        yield from notes_with_tag

    def delete(self, note_id: int):
        if note_id in self.notes:
            del self.notes[note_id]
            return messages.SUCCESS_DELETING_NOTE_MESSAGE.format(note_id)
        else:
            raise ValueError(messages.NOTE_NOT_FOUND_MESSAGE)

    def edit_in_editor(self, note_id):
        note = self.get(note_id)
        if not note:
            raise ValueError(messages.NOTE_NOT_FOUND_MESSAGE)

        text = TextArea(text=note.content or "", multiline=True, scrollbar=True, wrap_lines=False)
        status_bar = Label("  Ctrl-S: Save   Ctrl-Q: Quit", style="class:status")
        layout = HSplit([text,status_bar])
        style = Style.from_dict({"status": "reverse"})

        kb = KeyBindings()

        @kb.add("c-s")
        def _(event): event.app.exit(result=text.text)

        @kb.add("c-q")
        def _(event): event.app.exit(result=None)

        app = Application(layout=Layout(layout), key_bindings=kb, full_screen=True, style=style)
        new_content = app.run()

        if new_content.strip() != note.content.strip():
            note.edit(new_content)
            return messages.SUCCESS_UPDATING_NOTE_MESSAGE.format(note.value, note_id)
        else:
            return messages.NO_CHAGES_WAS_MADE_MESSAGE
