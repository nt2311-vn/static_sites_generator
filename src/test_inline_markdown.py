import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", "text_type_text")
        new_nodes = split_nodes_delimiter(node, "**", "text_type_bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text_type_text"),
                TextNode("bolded", "text_type_bold"),
                TextNode("word", "text_type_text"),
            ],
            new_nodes,
        )
