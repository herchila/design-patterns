class HtmlElement:
    def accept(self, visitor): pass


class HtmlParagraph(HtmlElement):
    def accept(self, visitor):
        visitor.visit_paragraph(self)


class HtmlAnchor(HtmlElement):
    def accept(self, visitor):
        visitor.visit_anchor(self)


class Visitor:
    def visit_paragraph(self, paragraph): pass
    def visit_anchor(self, anchor): pass


class RenderVisitor(Visitor):
    def visit_paragraph(self, paragraph):
        print("<p>Paragraph content</p>")

    def visit_anchor(self, anchor):
        print("<a href='url'>Anchor text</a>")


# Usage
# Client code
paragraph = HtmlParagraph()
anchor = HtmlAnchor()

render_visitor = RenderVisitor()

paragraph.accept(render_visitor)
anchor.accept(render_visitor)
