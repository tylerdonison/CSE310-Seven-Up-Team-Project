import random
from problem import Problem
#programming overseen by Jake
#data for difficulties overseen by Cheryl

#class for handling word module, will include difficultly, problems, etc.

class Word(Problem):
  
  def __init__(self, difficulty):
    super().__init__()
    self.word = ""
    self.difficulty = ""
    self.word_list = self._generate_word_list(difficulty)
    
  def _generate_word_list(self, difficulty):
    word_list = []
    return word_list
    
  def generate_sentence(self, nouns, verbs, subjects):
    pass