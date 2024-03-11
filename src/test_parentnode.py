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
