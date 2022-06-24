from problem import Problem
import random

class Sentence(Problem):

    def __init__(self, nouns, verbs, prepositions, articles):
        super.__init__()
        self._noun = ""
        self._verb = ""
        self._object = ""
        self._preposition = ""
        self._article = ""
        self._nouns = nouns
        self._verbs = verbs
        self._prepositions = prepositions
        self._articles = articles

    def _select_words(self):
        """Randomly selects sentence parts"""
        self._noun = random.choice(self._nouns)
        self._verb = random.choice(self._verbs)
        self._object = random.choice(self._nouns)
        self._preposition = random.choice(self._prepositions)
        self._article = random.choice(self._articles)

    def _create_problem(self):
        """sets the value of problem to a sentence"""
        self.problem = (f"{self._preposition} {self._article} {self._noun} {self._verb} {self._object}.")
        self._solution = self.problem