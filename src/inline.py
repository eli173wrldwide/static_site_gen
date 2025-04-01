import re
from enum import Enum
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_nodes = []
    

    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            result_nodes.append(node)
        else:
            parts_list = node.text.split(delimiter)

            if len(parts_list) % 2 == 0: 
                raise Exception (f"Invalid Markdown syntax: Unclosed delimiter {delimiter}")
            else:
                for i in range(len(parts_list)):
                    if parts_list[i] != "":
                        if i % 2 == 0:
                            result_nodes.append(TextNode(parts_list[i], TextType.TEXT))
                        else:
                            result_nodes.append(TextNode(parts_list[i], text_type))
    
    return result_nodes

def extract_markdown_images(text):
    matches = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = []
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    result_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            result_nodes.append(TextNode(node.text, node.text_type))
        else: 
            split_nodes = re.split(r"(!\[.*?\]\(.*?\))", node.text)
            for line in split_nodes:
                if line.startswith("!["): 
                    line_image_tuple = extract_markdown_images(line)
                    result_nodes.append(TextNode(line_image_tuple[0][0], TextType.IMAGE, line_image_tuple[0][1]))
                elif line: 
                    result_nodes.append(TextNode(line, node.text_type))
    
    return result_nodes 


def split_nodes_link(old_nodes):
    result_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            result_nodes.append(TextNode(node.text, node.text_type))
        else: 
            split_nodes = re.split(r"(\[.*?\]\(.*?\))", node.text)
            for line in split_nodes:
                if line.startswith("[") and re.match(r"\[.*?\]\(.*?\)", line):
                    line_link_tuple = extract_markdown_links(line)
                    result_nodes.append(TextNode(line_link_tuple[0][0], TextType.LINK, line_link_tuple[0][1]))
                elif line: 
                    result_nodes.append(TextNode(line, node.text_type))
    
    return result_nodes

def text_to_textnodes(text):
    full_node_list = []  # This will hold all properly processed TextNodes

    delimiters_and_types = [
        ("**", TextType.BOLD),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE),
    ]

    # Step 1: Process basic delimiters
    for delimiter, text_type in delimiters_and_types:
        nodes = split_nodes_delimiter(text, delimiter, text_type)  # Split with current delimiter
        
        # Step 2: Sort through nodes
        for node in nodes:
            if node.text_type == TextType.TEXT:  # Only unformatted text needs further handling
                # Refine by splitting for images/links
                image_nodes = split_nodes_image(node)  # Handle images in text
                for image_node in image_nodes:
                    link_nodes = split_nodes_link(image_node)  # Handle links in text or images
                    full_node_list.extend(link_nodes)  # Add final refined nodes
            else:
                # Already handled types (BOLD, ITALIC, CODE)
                full_node_list.append(node)
    
    return full_node_list
