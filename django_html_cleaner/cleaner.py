from lxml import etree
from lxml.html import tostring, fromstring
from lxml.html.clean import Cleaner as LxmlCleaner
import re

find_styled_elements = etree.XPath("descendant-or-self::*[@style]")
find_empty_text_nodes = etree.XPath("//text()[normalize-space()='']")


class Cleaner:

    """
    Cleans HTML to remove offending tags, attributes, or styles.
    Takes the following attributes:

    ``allowed_tags``:
        If ``allowed_tags`` is not set, all valid HTML tags except ``script``
        are accepted.

    ``allowed_attributes``:
        If ``allowed_attributes`` is not set, all attributes are accepted
        except those that would trigger JavaScript.

    ``allowed_styles``:
        If ``allowed_styles`` is not set, all styles are accepted.

    JavaScript is _always_ removed.
    """

    def __init__(self, allowed_tags=None, allowed_attributes=None,
                 allowed_styles=None, strip=False):
        self.allowed_tags = allowed_tags
        self.allowed_attributes = allowed_attributes
        self.allowed_styles = allowed_styles
        self.strip = strip

        remove_unknown_tags = allowed_tags is not None
        safe_attrs_only = allowed_attributes is not None

        self.cleaner = LxmlCleaner(allow_tags=allowed_tags,
                                   remove_unknown_tags=remove_unknown_tags,
                                   safe_attrs_only=safe_attrs_only,
                                   safe_attrs=allowed_attributes)

    def __call__(self, html):
        doc = fromstring(html)
        self.cleaner(doc)

        for el in find_styled_elements(doc):
            old_style = el.get('style')
            new_style = self.sanitize_css(old_style)
            if old_style != new_style:
                el.set('style', new_style)

        for el in find_empty_text_nodes(doc):
            el.getparent().tail = None

        return tostring(doc, pretty_print=False, encoding="unicode")

    def sanitize_css(self, style):
        """Whitelist only the given styles."""

        def is_property_allowed(prop):
            """Check to see if property is in allowed styles.
               If allowed styles is not set, all properties are allowed."""
            return self.allowed_styles is None or \
                prop.lower() in self.allowed_styles

        # disallow all urls
        style = re.compile(r'url\s*\(\s*[^\s)]+?\s*\)\s*').sub(' ', style)

        if not re.match(r"^\s*([-\w]+\s*:[^:;]*(;\s*|$))*$", style):
            return ''

        clean = []
        for prop, value in re.findall(r'([-\w]+)\s*:\s*([^:;]*)', style):
            if not value:
                continue
            if is_property_allowed(prop):
                clean.append(prop + ': ' + value + ';')

        return ' '.join(clean)
