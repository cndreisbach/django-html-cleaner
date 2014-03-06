import unittest

from lxml.html import fromstring, tostring
from django_html_cleaner.cleaner import Cleaner


def normalize(html):
    return tostring(fromstring(html), encoding="utf-8")

n = normalize


class TestCleaner(unittest.TestCase):

    def setUp(self):
        pass

    def test_cleaner_with_no_args_removes_js(self):
        cleaner = Cleaner()
        html = """<p onclick="alert()">Hello world!</p>
                  <p>How are you?</p>
                  <script src="/scripts/whoa.js"></script>"""
        expected = "<div><p>Hello world!</p><p>How are you?</p></div>"
        cleaned_html = cleaner(html)
        self.assertEqual(cleaned_html, expected)

    def test_cleaner_with_no_args_allows_styles(self):
        cleaner = Cleaner()
        html = """<p style="font-weight: bold; color: #333;">Hi there!</p>"""
        expected = html
        cleaned_html = cleaner(html)
        self.assertEqual(cleaned_html, expected)

    def test_cleaner_can_eliminate_styles(self):
        cleaner = Cleaner(allowed_styles=['font-weight', 'text-decoration'])
        html = """<p style="font-weight: bold; color: #333;">Hi there!</p>"""
        expected = """<p style="font-weight: bold;">Hi there!</p>"""
        cleaned_html = cleaner(html)
        self.assertEqual(cleaned_html, expected)

    def tearDown(self):
        pass
