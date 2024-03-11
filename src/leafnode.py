from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required for LeafNode")

        props_html = f"{self.props_to_html()}" if self.props else ""
        return f"<{self.tag} {props_html}>{self.value}</{self.tag}>" if self.tag else f"{self.value}"
