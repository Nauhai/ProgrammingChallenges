import unittest
import markov
from markov import Word


class TestMarkov(unittest.TestCase):
    maxDiff = None

    def test_get_words(self):
        input = "Lorem ipsum dolor sit amet."
        words = markov.get_words(input)
        self.assertEqual(words, [Word("Lorem", starting=True), Word("ipsum"), Word("dolor"), Word("sit"), Word("amet", ending=True)])

    def test_get_words_repetitive(self):
        input = "A B C D. B D C A."
        words = markov.get_words(input)
        self.assertEqual(words, [Word("A", starting=True), Word("B"), Word("C"), Word("D", ending=True), Word("B", starting=True), Word("D"), Word("C"), Word("A", ending=True)])

    def test_get_graph(self):
        input = "A B C D. B D C A."
        words = dict(markov.get_graph(input))
        self.assertDictEqual(words, {
            Word("A", starting=True): [Word("B")],
            Word("B"): [Word("C")],
            Word("C"): [Word("D", ending=True), Word("A", ending=True)],
            Word("B", starting=True): [Word("D")],
            Word("D"): [Word("C")],
        })

    def test_compute_all_sentences_from(self):
        graph = {
            Word("A", starting=True): [Word("B", ending=True), Word("C", ending=True)]
        }
        sentences = markov.compute_all_sentences_from(graph, Word("A", starting=True), 10)
        self.assertEqual(sentences, [["A", "B"], ["A", "C"]])

    def test_compute_all_sentences_from_max_length(self):
        graph = {
            Word("A", starting = True): [Word("B")],
            Word("B"): [Word("B"), Word("C", ending=True)]
        }
        sentences = markov.compute_all_sentences_from(graph, Word("A", starting=True), 5)
        self.assertEqual(sentences, [["A", "B", "B", "B", "C"], ["A", "B", "B", "C"], ["A", "B", "C"]])

    def test_compute_all_sentences(self):
        graph = {
            Word("A", starting=True): [Word("B", ending=True), Word("B", ending=True), Word("C", ending=True)]
        }
        sentences = dict(markov.compute_all_sentences(graph, 10))
        self.assertDictEqual(sentences, {
            ("A", "B"): 2,
            ("A", "C"): 1
        })


if __name__ == "__main__":
    unittest.main()
