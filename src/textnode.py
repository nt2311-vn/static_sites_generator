from leafnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_text_node) -> bool:
        return (
            self.text == other_text_node.text
            and self.text_type == other_text_node.text_type
            and self.url == other_text_node.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        switcher = {
            "case_text_text": LeafNode(None, self.text, None).to_html(),
            "case_text_bold": LeafNode("b", self.text, None).to_html(),
            "case_text_italic": LeafNode("i", self.text, None).to_html(),
            "case_text_link": LeafNode("a", self.text, {"href": self.url}).to_html(),
            "case_text_code": LeafNode("code", self.text, None).to_html(),
            "case_text_image": LeafNode(
                "img", "", {"src": self.url, "alt": self.text}
            ).to_html(),
        }

        return switcher.get(self.text_type, "Non supported text type.")
