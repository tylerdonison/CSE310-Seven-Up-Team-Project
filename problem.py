from abc import ABC, abstractmethod
class Problem():
  """Parent class to set defaults for the math and word modules.
  """
  
  def __init__(self):
    self.problem = ""
    self._solution = ""
    self._difficulty = 0
  
  def check_solution(self, user_answer):
    """Returns true if input answer is correct"""
    return user_answer == self._solution
  
  def set_difficulty(self, difficulty):
    """Sets the difficulty of the next level"""
    self._difficulty = difficulty

  
  @abstractmethod
  def _setup_difficulty(self):
    pass
