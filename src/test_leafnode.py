import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_render_raw_test(self):
        leaf_node = LeafNode(None, "Raw string")
        actual = leaf_node.to_html()
        expected = "Raw string"
        self.assertEqual(actual, expected)

    def test_render_no_props(self):
        leaf_node = LeafNode("h1", "This is a big title")
        actual = leaf_node.to_html()
        expected = "<h1>This is a big title</h1>"
        self.assertEqual(actual, expected)

    def test_render_with_props(self):
        leaf_node = LeafNode(
            "p",
            "This is a red line with italic text",
            props={"class": "red", "style": "italic"},
        )

        actual = leaf_node.to_html()
        expected = (
            "<p class='red' style='italic' >This is a red line with italic text</p>"
        )
        self.assertEqual(actual, expected)
