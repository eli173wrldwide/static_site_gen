from textnode import TextType, TextNode


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(f" {key}=\"{value}\"" for key, value in self.props.items())

    def __repr__(self):
        return f"{self.tag} = tag, {self.value} = value, {self.children} = children, {self.props} = props"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        else:
            attributes = self.props_to_html()
            return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"   

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode is missing a tag.")
        if self.children is None or not self.children:
            raise ValueError("ParentNode must have children.")
        else:
            leaf_nodes = "".join([leaf.to_html() for leaf in self.children]) 
            return f"<{self.tag}>{leaf_nodes}</{self.tag}>"

def text_node_to_html_node(text_node):
    mappings = {
    TextType.TEXT: lambda node: LeafNode(None, node.text),
    TextType.BOLD: lambda node: LeafNode("b", node.text),
    TextType.ITALIC: lambda node: LeafNode("i", node.text),
    TextType.CODE: lambda node: LeafNode("code", node.text),
    TextType.LINK: lambda node: LeafNode("a", node.text, {"href": node.url}),
    TextType.IMAGE: lambda node: LeafNode("img", "", {"src": node.url, "alt": node.text}),
    }
    
    if text_node.text_type in mappings:
        return mappings[text_node.text_type](text_node)
    else:
        raise Exception("Invalid TextType")
