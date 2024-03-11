from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag attribute is required")
        if not self.children:
            raise ValueError("children attribute is required")

        children_html = f"<{self.tag} {self.props_to_html()}>"

        for child in self.children:
            children_html += child.to_html()

        children_html += f"</{self.tag}>"
        return children_html
