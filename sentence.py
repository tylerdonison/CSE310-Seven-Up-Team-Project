from problem import Problem
import random

class Sentence(Problem):

    def __init__(self, nouns, verbs, prepositions, articles):
        super().__init__()
        self._noun = ""
        self._verb = ""
        self._object = ""
        self._preposition = ""
        self._article = ""
        self._nouns = nouns
        self._verbs = verbs
        self._prepositions = prepositions
        self._articles = articles

    def setup_sentence(self):
        self._select_words()
        self._setup_difficulty()
        self._create_problem()

    def _select_words(self):
        """Randomly selects sentence parts"""
        self._noun = random.choice(self._nouns)
        self._verb = random.choice(self._verbs)
        self._object = random.choice(self._nouns)
        self._preposition = random.choice(self._prepositions)
        self._article = random.choice(self._articles)

    def _create_problem(self):
        """sets the value of problem to a sentence"""
        # check sentence parts to see if they are included in the sentence
        sentence_parts = [self._preposition, self._article, self._noun, self._verb, self._object]
        for i in range (len(sentence_parts) -1):
            if sentence_parts[i] != "":
                self.problem += sentence_parts[i]
            
                # check to see if we are at the end of the sentence for spaces
                if i < len(sentence_parts) - 1:
                    self.problem += " "
    
        self._solution = self.problem
    
    def _setup_difficulty(self):
        if self._difficulty == 1:
            self._preposition = ""
            self._article = ""
            self._object = ""
        
        if self._difficulty == 2:
            self._preposition = ""
            self._article = ""
        
        