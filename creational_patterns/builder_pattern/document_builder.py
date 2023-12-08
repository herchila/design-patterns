class Document:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def __str__(self):
        return '\n'.join(self.parts)

class Builder:
    def build_title(self, title): pass
    def build_body(self, body): pass
    def get_result(self): pass

class TextBuilder(Builder):
    def __init__(self):
        self.document = Document()

    def build_title(self, title):
        self.document.add(f"Title: {title}")

    def build_body(self, body):
        self.document.add(body)

    def get_result(self):
        return self.document

# Usage
builder = TextBuilder()
builder.build_title("My Title")
builder.build_body("Hello, world!")
document = builder.get_result()
print(document)

# Output:
# Title: My Title
# Hello, world!
