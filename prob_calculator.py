import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**balls):
    self.contents = []
    for key,value in balls.items():
      self.contents.extend([key for i in range(value)])

  def draw(self,remove):
    removed = []
    for i in range(min(remove, len(self.contents))):
      rand = random.randrange(len(self.contents))
      removed.append(self.contents.pop(rand))
    return removed
      
      


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    experiment = copy.deepcopy(hat)
    removedList = experiment.draw(num_balls_drawn)
    removedObj = {}
    for ball in removedList:
      if ball in removedObj:
        removedObj[ball] += 1
      else:
        removedObj[ball] = 1
    included = True
    for ball, n in expected_balls.items():
      if ball not in removedObj or removedObj[ball] < n:
        included = False

    if included:
      M += 1    

  return M/num_experiments
  
