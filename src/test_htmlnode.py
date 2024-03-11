import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_toHTML_have_props(self):
        html_node = HTMLNode(props={"class": "bold", "id": "title"})
        actual = html_node.props_to_html()
        expected = " class = 'bold' id = 'title' "
        self.assertEqual(actual, expected)

    def test_props_toHTML_none_props(self):
        html_node = HTMLNode()
        actual = html_node.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)
