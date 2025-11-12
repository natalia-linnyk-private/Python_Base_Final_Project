from src.data_models.notes_manager import NotesManager


def add_note(args, notes: NotesManager):
    title = " ".join(args)
    if len(title) == 0:
        return "Title is required."
    note_id = notes.new(title)
    return f"Created note: {note_id}"


def edit_note(args, notes: NotesManager):
    note_id, *_ = args
    return notes.edit_in_editor(int(note_id))


def delete_note(args, notes: NotesManager):
    note_id, *_ = args
    return notes.delete(int(note_id))

def list_notes(notes: NotesManager):
    return str(notes)