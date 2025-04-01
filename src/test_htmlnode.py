import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_leafnode_to_html_valid(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(None, "Hello!")
        self.assertEqual(node.to_html(), "Hello!")  # No wrapping tag, just the value
    
    def test_leafnode_to_html_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("a", None)
            node.to_html()
    

class TestParentNode(unittest.TestCase):
    def test_basic_parent_with_children(self):
        child_node = LeafNode("b", "bold")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><b>bold</b></div>")

    def test_parent_without_tag_raises_error(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode(None, [LeafNode("b", "bold")])
            parent_node.to_html()
        self.assertEqual(str(context.exception), "ParentNode is missing a tag.")

    def test_parent_without_children_raises_error(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("div", [])
            parent_node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children.")
  
    def test_multiple_children(self):
        children = [
            LeafNode("i", "italic"),
            LeafNode(None, "plain text"),
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(parent_node.to_html(), "<p><i>italic</i>plain text</p>")

    def test_nested_parent_nodes(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_empty_grandchild_raises_error(self):
        with self.assertRaises(ValueError) as context:
            grandchild = ParentNode("span", [])
            parent = ParentNode("div", [grandchild])
            parent.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children.")


class TestTextNodeToHTMLNode(unittest.TestCase):
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")           



if __name__ == "__main__":
    unittest.main()
