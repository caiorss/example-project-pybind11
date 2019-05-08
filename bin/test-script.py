
import test2 as t 

class Dummy:
  def __init__(self, name):
      self.name = name
      
  def call(self, x):
      return 4.5 * x + 10

d = Dummy("DUMMY-OBJECT")

print("\n======= Running: t.callPyObjectMethod(d, 4.50) =========")
t.callPyObjectMethod(d, 4.50)

print("\n======= Running: t.callPyObjectMethod(d, 100.0) =========")
t.callPyObjectMethod(d, 100.0)


