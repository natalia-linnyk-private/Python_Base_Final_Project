class NoteRecord:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags or []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def match(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.content.lower()
