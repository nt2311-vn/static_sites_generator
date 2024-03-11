import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://google.com")
        self.assertNotEqual(node, node2)

    def test_diff_text_type(self):
        node = TextNode("This is a text node", "bold", "https://google.com")
        node2 = TextNode("This is a text node", "italic", "https://google.com")
        self.assertNotEqual(node, node2)

    def test_tohtml_image(self):
        node = TextNode(
            "Dog image",
            "text_type_image",
            "https://th.bing.com/th/id/OIP.XGvRwx1I7qo-wuVZUfCOWAHaEo?rs=1&pid=ImgDetMain",
        )
        actual = node.text_node_to_html_node()
        expected = "<img src = 'https://th.bing.com/th/id/OIP.XGvRwx1I7qo-wuVZUfCOWAHaEo?rs=1&pid=ImgDetMain' alt = 'Dog image' >"
        self.assertEqual(actual, expected)

    def test_tohtml_code(self):
        node = TextNode("console.log('Hello World')", "text_type_code", None)
        actual = node.text_node_to_html_node()
        expected = "<code>console.log('Hello World')</code>"
        self.assertEqual(actual, expected)

    def test_tohtml_unsupported(self):
        node = TextNode("This is a text node", "random", "https://google.com")

        with self.assertRaises(Exception) as context:
            node.text_node_to_html_node()

        self.assertEqual(str(context.exception), "Unsupported text type")
