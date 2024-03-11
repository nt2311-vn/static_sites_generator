from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag attribute is required")

        if len(self.children) == 0:
            raise ValueError("children attribute must not be empty list")
