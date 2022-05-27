import random
from problem import Problem
#programming overseen by Jake
#data for difficulties overseen by Cheryl

#class for handling word module, will include difficultly, problems, etc.

class Word(Problem):
  
  __init__(difficulty):
    word = ""
    difficulty = ""
    word_list = generate_word_list(difficulty)
    
    generate_word_list(difficulty):
      word_list = []
      
      return word_list
    
    #generate_sentence(nouns, verbs, subjects):
    
