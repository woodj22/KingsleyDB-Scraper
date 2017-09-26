import unittest

from kingsley_scraper.scraper import reader
import html


class ReaderUnitTest(unittest.TestCase):
    def test_retrieve_tag_and_weights_returns_an_array_of_strings_in_the_tag(self):
        sentence_string = "tiger lays low in the dirty forest"
        content = html.unescape('<html><h1>'+sentence_string+'</h1></html>')
        h1_weight = reader.tag_weight('h1')
        actual_result = reader.retrieve_tag_and_weights(content)
        expected_result = [(word, h1_weight) for word in sentence_string.split(' ')]

        self.assertListEqual(expected_result, actual_result)

    def test_retrieve_tag_and_weight_returns_an_array_of_strings_in_the_tag_when_their_are_two_of_the_same_tags_in_html(self):
        sentance_string = "tiger lays"
        sentance_string_1 = "hello"
        h1_weight = reader.tag_weight('h1')
        content = html.unescape('<html><h1>' + sentance_string + '</h1><h1>' + sentance_string_1 + '</h1></html>')
        actual_result = reader.retrieve_tag_and_weights(content)
        expected_result = [('tiger', h1_weight), ('lays', h1_weight), ('hello', h1_weight)]

        self.assertListEqual(expected_result, actual_result)


    def test_get_tag_strings_returns_a_list_of_tuples_containing_tag_and_string(self):
        sentence_string = "tiger lays low in the dirty forest"
        content = html.unescape("<html><h1>"+sentence_string+"<h3><h2>saf</h2></h3></h1></html>")
        actual_result = reader.get_tag_strings(content)
        expected_result = [('h1', ['tiger', 'lays', 'low', 'in', 'the', 'dirty', 'forest']), ('h2', ['saf'])]

        self.assertListEqual(expected_result, actual_result)

    def test_retrieve_tag_and_weight_returns_a_list_of_tuples_containing_a_weight_string_pair(self):
        sentence_string = "tiger lays"
        content = html.unescape("<html><h1>" + sentence_string + "<h3><h2>saf</h2></h3></h1></html>")
        actual_result = reader.retrieve_tag_and_weights(content)

        expected_result = [('tiger', reader.tag_weight('h1')), ('lays', reader.tag_weight('h1')), ('saf', reader.tag_weight('h2'))]
        self.assertListEqual(expected_result, actual_result)


