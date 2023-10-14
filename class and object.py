class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

a1 = Person("alice", 25)
a2 = Person("bob","30")

print(a1.name,a1.age)
print(a2.name,a2.age)
