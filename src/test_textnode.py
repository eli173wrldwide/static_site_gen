import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "None")
        node2 = TextNode("This is a text node", TextType.BOLD, "None")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "www.urlit")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.urlit")
        self.assertNotEqual(node, node2) 

        node = TextNode("This is a text node", TextType.BOLD, "www.urlit")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.urlit")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
