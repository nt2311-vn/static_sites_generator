class TextNode:
    def __init__(self, text, text_type, url):
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
