import random
from problem import Problem
#programming overseen by Jake
#data for difficulties overseen by Cheryl

#class for handling word module, will include difficultly, problems, etc.

class Word(Problem):
  
  def __init__(self, words=[], nouns=[], verbs=[], prepositions=[], articles=[]):
    self._noun = ""
    self._verb = ""
    self._object = ""
    self._preposition = ""
    self._article = ""
    self._nouns = nouns
    self._verbs = verbs
    self._prepositions = prepositions
    self._articles = articles

    self._words = words
    self._word = ""

  def setup_sentence(self):
    self._select_words()
    self._create_problem()
    

  def _select_words(self):
    """randomly selects sentance parts"""

    if len(self._words) == 0:
      self._noun = random.choice(self._nouns)
      self._verb = random.choice(self._verbs)
      self._object = random.choice(self._nouns)
      self._preposition = random.choice(self._prepositions)
      self._article = random.choice(self._articles)
    
    else:
      self._word = random.choice(self._words)

  def _create_problem(self):
    if len(self._words) == 0:
      self.problem = (f"{self._preposition} {self._article} {self._noun} {self._verb} {self._object}.")
    
    else:
      self.problem = self._word
    
    self._solution = self.problem
  

  

''' 
while(True):      
  nouns = ["boy", "girl", "dog", "apple", "horse"]
  verbs = ["ran", "fought", "jumped"]
  prepositions = ["about", "above", "across", "after", "along",
          "around", "at", "before", "behind", "below",
          "beyond", "by", "despite", "except", "for",
          "from", "in", "into", "near", "of",
          "off", "on", "onto", "out", "over",
          "past", "to", "under", "with", "without"]

  articles = ["a", "the"]

  word = Word(nouns, verbs, prepositions, articles)

  word.setup_sentence()
  print(word.problem)
  solution = input("> ")
  print(word.check_solution(solution))
  '''
