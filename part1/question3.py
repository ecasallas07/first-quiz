################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
class materials:
  def __init__(self):
    self.type = 0
    self.temperature = 0
    
  def add(self,items):
      if "lead" in items or "mercury" in items:
          self.type = 1
      elif "water" in items or "air" in items:
          self.type = 2
      elif "cheese" in items or "dough" in items or "tomato" in items:
          self.type = 3
  
  def freeze(self):
      self.temperature = 2
  
  def boil(self):
     self.temperature = 1 
  
  def wait(self):
    #  print("Ingreso aqui 0")
     self.temperature = 0
    
    
  def get_output(self):
      if self.temperature == 1 and self.type == 1:
        return "gold"
      elif self.temperature == 2 and self.type == 2:
        return "snow"
      elif self.temperature == 1 and self.type == 3:
        return "pizza"  
      else:
        return "unknown"  

def make_oven():
  oven = materials()
  return oven

def alchemy_combine(oven, ingredients, temperature):

  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()
  return oven.get_output()
      