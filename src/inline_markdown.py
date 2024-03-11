import re
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimeter, text_type):
    md_text_dict = {
        "text_type_code": "code",
        "text_type_bold": "bold",
        "text_type_text": "text",
        "text_type_italic": "italic",
    }

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != md_text_dict[text_type]:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimeter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, bold section not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue

            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], "text_type_text"))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes
