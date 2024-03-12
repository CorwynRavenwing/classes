import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    retval = 0
    att = node.attrib
    # print("#N", node.tag, len(att))
    retval += len(att)
    for child in node:
        retval += get_attr_number(child)
    return retval

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

