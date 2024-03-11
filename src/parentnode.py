from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
        if not self.children or len(self.children) == 0:
            raise ValueError("children attribute must not be empty list")

    def to_html(self):
        if not self.tag:
            raise ValueError("tag attribute is required")

        opening_tag = (
            f"<{self.tag} {self.props_to_html()}>" if self.props else f"<{self.tag}>"
        )
        closing_tag = f"</{self.tag}>"
        children_html = "".join(child.to_html() for child in self.children)

        return f"{opening_tag}{children_html}{closing_tag}"
