import unittest
from scraper.reader import get_tags
import html


class MyTest(unittest.TestCase):
    def test_get_tags_returns_an_array_of_strings_in_the_tag(self):
        sentance_string = "tiger lays low in the dirty forest"
        content = html.unescape('<html> <h1>'+sentance_string+'</h1></html>')

        actual_result = get_tags(content, 'h1')
        expected_result = sentance_string.split(' ')

        self.assertListEqual(expected_result, actual_result)

# if __name__ == '__main__':
#     unittest.main()