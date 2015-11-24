from __future__ import print_function

import xml.etree.ElementTree as ET

__version__ = "0.1"


def elements_equal(first, *others):
    f = first
    for e in others:
        if f.tag != e.tag or f.text != e.text or f.tail != e.tail or f.attrib != e.attrib or (not all(map(equal, list(f), list(e)))):
            return False
    return True


def get_element(text_or_tree_or_element):
    if isinstance(text_or_tree_or_element, ET.Element):
        return text_or_tree_or_element
    elif isinstance(text_or_tree_or_element, ET.ElementTree):
        return text_or_tree_or_element.getroot()
    elif isinstance(text_or_tree_or_element, basestring):
        return ET.fromstring(text_or_tree_or_element)
    else:
        return ET.parse(text_or_tree_or_element).getroot()


def equal(*xml):
    return elements_equal(*map(get_element, xml))

if __name__ == "__main__":
    import sys
    trees = []
    for fn in sys.argv[1:]:
        print("Parsing '%s'" % fn)
        trees.append(ET.parse(fn))
        print("done")
    print("Comparing")
    if equal(trees):
        print("All files are semantically equal")
        sys.exit()
    else:
        print("Not all files are semantically equal")
        sys.exit(1)
