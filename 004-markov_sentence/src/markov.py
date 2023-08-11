from dataclasses import dataclass
from collections import defaultdict, Counter
import random
import re


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
    input_text = input_text.strip()

    words = []

    cursor = 0
    current = ""
    starting = True
    ending = False

    while cursor < len(input_text):
        c = input_text[cursor]

        if c in (' ', '.') and current:
            if ending:
                # if previous word was ending, then current one is starting
                starting = True
                ending = False
            
            if c == '.':
                ending = True
            
            words.append(Word(current, starting, ending))
            current = ""
            starting = False
        
        elif c not in (' ', '.'):
            current += c
        
        cursor += 1

    return words


def get_graph(input_text: str) -> dict[Word, list[Word]]:
    words = get_words(input_text)

    graph = defaultdict(list)
    for i in range(len(words)-1):
        if not words[i].ending:
            graph[words[i]].append(words[i+1])
    
    return graph


def compute_all_sentences_from(graph, current, max_length):
    max_length -= 1

    if current.ending:
        return [[current.word]]
    
    if max_length == 0:
        return None
    
    all_sentences = []
    
    for word in graph[current]:
        sentences = compute_all_sentences_from(graph, word, max_length)
        if sentences:
            for i, s in enumerate(sentences):
                sentences[i] = [current.word] + s
            all_sentences.extend(sentences)
        
    return all_sentences


def compute_all_sentences(graph, max_length):
    all_sentences = []

    for starting_word in filter(lambda w: w.starting, graph.keys()):
        sentences = compute_all_sentences_from(graph, starting_word, max_length)
        all_sentences.extend(map(tuple, sentences))
    
    return Counter(all_sentences)
