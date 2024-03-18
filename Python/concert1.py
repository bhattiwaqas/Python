#intro to classes and objects

#define class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
    def birthday(self):
        self.age = self.age +1
    def getAge(self):
        return self.age

#Dog meatball = new Dog()

pers = []

#give name
pers1 = Person("Ramone", 88)
pers2 = Person("Jovanni", 50)
pers3 = Person("Lady Baba", 34)
pers4 = Person("Taylor Slow", 59)

pers = [pers1, pers2, pers3, pers4]

pers3.birthday()
pers3.birthday()

print("Here is everyone")
for i in pers:
    print(i.getAge() ) #print ages of all


pers1.age =89
print(pers1.age)
