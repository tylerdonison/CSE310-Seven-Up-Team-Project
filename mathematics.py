from problem import Problem
import random
import operator
#programming overseen by Jake
#data for difficulties overseen by Cheryl

#class for handling math module, will include difficultly, problems, etcs.

class Mathematics():
  def __init__(self):
    self._var_1 = 0
    self._var_2 = 0
    self.operator = "n"
    self.operation = "n"
    self.answer = "n"
    self.num_1 = "n"
    self.num_2 = "n"
    self.text = self.get_printed_problem()
    
    # self._operators = []
    # self._numbers = numbers

  def math_setup(self):
    self._set_random_vars()
    self._setup_difficulty()
    self._set_random_operator()
    self._find_solution()
    self._create_problem()
    
  def set_var(self, var_1, var_2):
    """Sets math variables by external parameter input"""
    self._var_1 = var_1
    self._var_2 = var_2

  def get_vars(self):
    """returns the values of the math variables"""
    return self._var_1, self._var_2
  
  def _set_random_operator(self):
    """randomly selects the math operator"""
    self._operator = random.choice(self._operators)
  
  def _set_random_vars(self):
    """randomly selects the math variables."""
    self._var_1 = random.choice(self._numbers)
    self._var_2 = random.choice(self._numbers)


  def _create_problem(self):
    """creates the math problem as a stringS"""

    self.problem = str(self._var_1) + " " + self._operator + " " + str(self._var_2)

  def _find_solution(self):
    """finds the solution to the math problem randomly generated"""
    if self._operator == "+":
      self._solution = self._var_1 + self._var_2
    
    elif self._operator == "-":
      self._solution = self._var_1 - self._var_2

    # If the problem is division, ensure solution is a whole number,
    # and ensure the divisor is not 0 
    elif self._operator == "/":
      self._check_divide_by_0()
      self._make_division_whole()
      self._solution = self._var_1 / self._var_2

    elif self._operator == "*":
      self._solution = self._var_1 * self._var_2



  def _check_divide_by_0(self):
    """Ensures problem does not divide by zero"""
    
    if self._var_2 == 0:
      self._var_2 += random.randrange(1, 10)

  def _make_division_whole(self):
    """makes sure the solution to division is a whole number"""
    remainder = self._var_1 % self._var_2

    if remainder == 0:
      return
    
    else:
      self._var_1 += self._var_2 - remainder
  
  def _setup_difficulty(self):
    if self._difficulty == 1:
      self._operators = ["+"]
    
    elif self._difficulty == 2:
      self._operators = ["+", "-"]
    
    elif self._difficulty == 3:
      self._operators = ["+", "-", "*"]
    
    elif self._difficulty > 3:
      self._operators = ["+", "-", "*", "/"]
    

  def produce_math_problem(self, diff):
    if diff == "easy":
      self.operators = {
        '+': operator.add,
        '-': operator.sub
      }
    elif diff == "medium":
      self.operators = {
        '+': operator.add,
        '-': operator.sub
      }
    
    elif diff == "hard":
      self.operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
      }
    
    self.num_1 = random.randint(1, 10)
    self.num_2 = random.randint(1, 10)
    self.operation = random.choice(list(self.operators.keys()))
    self.answer = self.operators.get(self.operation)(self.num_1, self.num_2)

    if diff == "easy":
        if self.answer < 0:
          self.produce_math_problem(diff)

  def get_printed_problem(self):
    text_list = [self.num_1,self.operation, self.num_2]
    self.text = ""
    for i in text_list:
      self.text += str(i)
    return self.text

  def get_answer(self):
    return str(self.answer)
'''
done = False
while not done:
  math_problem = Mathematics([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

  math_problem.math_setup()
  print(math_problem.problem)
  answer = input("> ")
  if answer.isalpha():
    done = True
  else:
    print(math_problem.check_answer(int(answer)), math_problem._solution)
'''
