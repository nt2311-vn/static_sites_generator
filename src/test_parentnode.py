import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_eq(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("span", "Red span text", {"style": "color: red;"}),
            ],
            None,
        )
        actual = parent_node.to_html()
        expected = "<p><b>Bold text</b>Normal text<span style = 'color: red;' >Red span text</span></p>"
        self.assertEqual(actual, expected)

    def test_parent_noprops(self):
        parent_node = ParentNode(
            "h1", [LeafNode(None, "Heading"), LeafNode("span", 1)], None
        )

        actual = parent_node.to_html()
        expected = "<h1>Heading<span>1</span></h1>"

        self.assertEqual(actual, expected)

    def test_parent_both_props(self):
        parent_node = ParentNode(
            "div",
            [
                LeafNode("h1", "Heading 1", {"style": "color: purple;"}),
                LeafNode("p", "First paragraph"),
                LeafNode("p", "Second paragraph"),
            ],
            {"align": "center", "padding": "10px"},
        )

        actual = parent_node.to_html()
        expected = "<div align = 'center' padding = '10px' ><h1 style = 'color: purple;' >Heading 1</h1><p>First paragraph</p><p>Second paragraph</p></div>"
        self.assertEqual(actual, expected)
