from __future__ import print_function

import xml.etree.ElementTree as ET
import sys

if sys.version_info >= (3, 0):
    unicode = str

__version__ = "0.2"


def elements_equal(first, *others):
    """
    Check elements for equality
    """
    f = first
    lf = list(f)
    for e in others:
        le = list(e)
        if (len(lf) != len(le)
                or f.tag != e.tag
                or f.text != e.text
                or f.tail != e.tail
                or f.attrib != e.attrib
                or (not all(map(elements_equal, lf, le)))
                ):
            return False
    return True


def get_element(text_or_tree_or_element):
    """
    Get back an ET.Element for several possible input formats
    """
    if isinstance(text_or_tree_or_element, ET.Element):
        return text_or_tree_or_element
    elif isinstance(text_or_tree_or_element, ET.ElementTree):
        return text_or_tree_or_element.getroot()
    elif isinstance(text_or_tree_or_element, (unicode, bytes)):
        return ET.fromstring(text_or_tree_or_element)
    else:
        return ET.parse(text_or_tree_or_element).getroot()


def equal(*xml):
    """
    Check xml elements/documants or strings for semantic equality by comparing a normalized representation (ElementTree).
    While this works well for 'normal' testing, there are different definitions of 'semantic equality' requiring different tools.
    """
    return elements_equal(*map(get_element, xml))

if __name__ == "__main__":
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
