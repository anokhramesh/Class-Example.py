# Create a class name Person  and Adding methods to a class
class Person:
  def __init__(self, name, age,gender,nationality,company,job):
    self.name = name
    self.age = age
    self.gender=gender
    self.nationality=nationality
    self.company=company
    self.job=job

p1 = Person("Ramesh", 50,"male","indian","dewa","Technician")
p2 = Person("Naheed",35,"male","Pakisthan","dewa","Asst Technician")
#Here p1 is an object
print(p2.name)
print(p2.age)
print(p2.gender)
print(p2.nationality)
print(p2.company)
print(p2.job)