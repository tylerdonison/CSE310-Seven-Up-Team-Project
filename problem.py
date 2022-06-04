
class Problem():
  """Parent class to set defaults for the math and word modules.
  """
  
  def __init__(self):
    self.problem = ""
    self._solution = ""
  
  def check_solution(self, user_answer):
    """Returns true if input answer is correct"""
    return user_answer == self._solution
