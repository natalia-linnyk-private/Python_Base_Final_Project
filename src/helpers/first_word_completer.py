from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer
from prompt_toolkit.document import Document

class FirstWordFilterCompleter(Completer):
    def __init__(self, word_completer):
        self.word_completer = word_completer
    
    def get_completions(self, document: Document, complete_event):
        if ' ' not in document.text_before_cursor:
            yield from self.word_completer.get_completions(document, complete_event)