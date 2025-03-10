import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
     
        node = HTMLNode("<p>", 15, ["list_v1", "list_v2"],)

        node = HTMLNode("This is a text node", "15", ["here_a_list", "and_yet_another"], {"hello": "hello_value", "second_key": "second_value"}) 

        node = HTMLNode("This is a text node", 15, [], {"hello": "hello_value", "second_key": "second_value"})

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

if __name__ == "__main__":
    unittest.main()
