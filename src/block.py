"""
This module takes markdown text and converts them to blocks, 
and then assigns a block type to them based on the type of block it is using the mapping

-2025-03-14
EH
"""

import re
from enum import Enum

def markdown_to_blocks(markdown):
    markdown_list = markdown.split("\n\n")
    clean_markdown =[]

    for item in markdown_list:
        if item != "":
            clean_markdown.append(item.strip())

    return clean_markdown

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(clean_markdown):

    mappings = {
            r"^\#{1,6}\s+": BlockType.HEADING, 
            r"^(```\s{1})[^```]+(\s{1}```)$": BlockType.CODE,
            r"^(```\s+```)$": BlockType.CODE,
            r"^>\s+": BlockType.QUOTE, 
            r"^-\s+": BlockType.UNORDERED_LIST,
            r"^\d+\.\s": BlockType.ORDERED_LIST,
        }
    for reg, block_type in mappings.items():
        if re.match(reg, clean_markdown):
            return block_type

    return BlockType.PARAGRAPH
