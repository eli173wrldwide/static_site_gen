from textnode import TextNode, TextType

def main():
    test_textnode = TextNode("here is some text", TextType.BOLD, "www.urltastic.com")
    print(test_textnode)
    return

if __name__ == "__main__":
    main()
