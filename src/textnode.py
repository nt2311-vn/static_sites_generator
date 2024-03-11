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
            "text_type_text": LeafNode(None, self.text, None).to_html(),
            "text_type_bold": LeafNode("b", self.text, None).to_html(),
            "text_type_italic": LeafNode("i", self.text, None).to_html(),
            "text_type_link": LeafNode("a", self.text, {"href": self.url}).to_html(),
            "text_type_code": LeafNode("code", self.text, None).to_html(),
            "text_type_image": LeafNode(
                "img", "", {"src": self.url, "alt": self.text}
            ).to_html(),
        }

        result = switcher.get(self.text_type)

        if result is None:
            raise Exception("Unsupported text type")

        return result
