# Copyright 2020 Alvaro Bartolome del Canto
# See LICENSE for details.


def is_visible(attr):
    """
    This function checks whether an HTML element attribute is visible or hidden based on
    the style of that HTML element. The purpose of this function in this package is to avoid
    including data that is useless, such as inner code markers, non-sense data, etc. So this
    function will ensure that we just retrieve useful data.

    Args:
        attr (:obj:`lxml.html.HtmlElement`): HTML element

    Returns:
        :obj:`bool` - flag
            This function returns either `True` or `False` depending on the style of the HTML element
            received from parameter, whether if it is visible or not, respectively.
    """

    if 'style' in attr.attrib:
        style = attr.get('style')
        if style.__contains__("display:none") or style.__contains__("display: none"):
            return False

    return True
