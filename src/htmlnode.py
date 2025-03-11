

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
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have child argument")
        else:
            leaf_nodes = "".join([leaf.to_html() for leaf in self.children]) 
            return f"<{self.tag}>{leaf_nodes}</{self.tag}>"

