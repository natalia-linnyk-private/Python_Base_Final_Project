import os
import pickle
import datetime
from tui_editor import TuiEditor
# need: pip install tui-editor

from src.data_models.record_fields import Field

class Note(Field):
    def __init__(self, title):
        super().__init__(title)
        self.content = ""
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def edit(self, new_content):
        self.content = new_content
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"Title: '{self.value}' updated {self.updated_at:%Y-%m-%d %H:%M}"


class NotesManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self._load()
        self.note_counter = 0 if len(self.notes) == 0 else max(self.notes.keys())+1

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        return {}

    def save(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.notes, f)

    def new(self, title):
        note_id = self.note_counter
        self.note_counter += 1
        note = Note(title)
        self.notes[note_id] = note
        return note_id


    def list_all(self):
        if not self.notes:
            yield "No notes yet."
            return
        for nid, note in self.notes.items():
            yield f"{nid}: {note.value} (updated {note.updated_at:%Y-%m-%d %H:%M})"

    def get(self, note_id: int):
        return self.notes.get(note_id)

    def delete(self, note_id: int):
        if note_id in self.notes:
            del self.notes[note_id]
            return f"Deleted note {note_id}"
        else:
            return "Note not found."


    def edit_in_editor(self, note_id):
        note = self.get(note_id)
        if not note:
            return "Note not found."

        editor = TuiEditor()
        editor.set_text(note.content or "")
        print("Press Ctrl-S to exit editor")
        editor.edit()
        new_content = editor.get_text()

        if new_content.strip() != note.content.strip():
            note.edit(new_content)
            return f"Updated note '{note.value}' ({note_id})"
        else:
            return "No changes made."

    def __str__(self):
        if not self.notes:
            raise ValueError("Note book is empty")

        result = ["Note Book:"]
        for id, note in self.notes.items():
            result.append(f"{int(id)}: {note}")
        return '\n'.join(result)
