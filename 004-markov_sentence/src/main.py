from dataclasses import dataclass
from collections import defaultdict
import re
import random


@dataclass
class Word:
    word: str
    starting: bool = False
    ending: bool = False

    def __key(self):
        return (self.word, self.starting, self.ending)

    def __hash__(self):
        return hash(self.__key())
    
    def __eq__(self, other):
        if isinstance(other, Word):
            return self.__key() == other.__key()
        return NotImplemented


def get_words(input_text: str) -> list[Word]:
    words = list(map(lambda w: Word(w), re.findall("\w+", input_text)))
    starting_words = re.findall("(?:(?:^|(?:\.(?: ?)))(?P<starting>\w+))", input_text)
    ending_words = re.findall("(?:(?P<ending>\w+)\.)", input_text)

    for w in words:
        if w.word in starting_words:
            w.starting = True
        if w.word in ending_words:
            w.ending = True
    
    return words


def get_graph(words: list[Word]):
    graph = defaultdict(lambda: list())
    for i in range(len(words)-1):
        graph[words[i]].append(words[i+1])
    return graph


def compute_sentence(graph: dict[Word, list[Word]]) -> list[Word]:
    current_word = random.choice(list(filter(lambda w: w.starting, graph.keys())))
    sentence = [current_word.word]
    while not current_word.ending:
        current_word = random.choice(graph[current_word])
        sentence.append(current_word.word)
    return sentence


if __name__ == "__main__":
    with open("src/input.txt", "r", encoding="utf-8") as file:
        text = file.read()
        words = get_words(text)
        graph = get_graph(words)
        sentence = compute_sentence(graph)
        print(' '.join(sentence) + '.')
