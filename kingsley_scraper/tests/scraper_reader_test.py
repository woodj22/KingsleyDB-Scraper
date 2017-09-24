import unittest

from kingsley_scraper.scraper import reader
import html


class ReaderUnitTest(unittest.TestCase):
    def test_get_tags_returns_an_array_of_strings_in_the_tag(self):
        sentance_string = "tiger lays low in the dirty forest"
        content = html.unescape('<html> <h1>'+sentance_string+'</h1></html>')
        actual_result = reader.get_tags(content, 'h1')
        expected_result = sentance_string.split(' ')

        self.assertListEqual(expected_result, actual_result)

    def test_get_tags_returns_an_array_of_strings_in_the_tag_when_their_are_two_of_the_same_tags_in_html(self):
        sentance_string = "tiger lays low in the dirty forest"
        sentance_string_1 = "Hello this is my best sentance."

        content = html.unescape('<html> <h1>' + sentance_string + '</h1> <h1>' + sentance_string_1 + '</h1></html>')
        actual_result = reader.get_tags(content, 'h1')
        expected_result = sentance_string.split(' ')

        self.assertListEqual(expected_result, actual_result)


    def test_get_tag_list_returns_a_list_of_all_tags_in_the_string(self):
        sentance_string = "tiger lays low in the dirty forest"
        content = html.unescape("<html><h1><h3><h2>saf</h2></h3></h1></html>")
        actual_result = reader.get_tag_list(content)
        expected_result = ['html', 'h1', 'h2', 'h3']
        self.assertListEqual(expected_result, actual_result)


