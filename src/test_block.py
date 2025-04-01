import unittest
from enum import Enum

from block import markdown_to_blocks, BlockType, block_to_block_type

class TestBlockSplit(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class testblocktoblocktype(unittest.TestCase):
    def test_block_to_blocktype(self):
        test_block = "this is **bolded** paragraph"
        
        block_tag = block_to_block_type(test_block)
        self.assertEqual(
            block_tag, BlockType.PARAGRAPH
        )
