class Person:
    number_of_person_initializated = 0
    def __init__(self, name, age, email, salary):
        self.name = name
        self.age= age
        self.email=email
        self.salary = salary
        Person.number_of_person_initializated += 1
    def fullName(self):
        print(f"My name is {self.name}")
    def raiseSalaty(self):
        print(f"the raised salay is {(self.salary*0.4)+self.salary}")


class Car:
    
    def __init__(self, size, wheels, doors, go_forward, go_backward, quiet):
        self.wheels = wheels
        self.size = size
        self.doors=doors
        self.go_forward = go_forward
        self.go_backward= go_backward
        self.quiet= quiet

        def _go_fordward(self):
            go_forward = True
            #quiet=False

#Normal class methods
myCar = Car(2, 4, 4, False, False, True)
print(myCar.__dict__)
myCar.go_forward()
print(myCar.__dict__)





""" print(f"The state of the car is {myCar.go_forward}")
myCar.go_forward=True
print(f"The state of the car is {myCar.go_forward}")


# Statics variables
print(f"\n\n The number of initializations at the moment is --> {Person.number_of_person_initializated}")
print("\n\n")
person1 = Person("Rox", 3, "Rox@gmail.com", 50000)
person1.raiseSalaty()
print(person1.__dict__)
person2 = Person("Sixz", 5, "Asizx@gmail.com", 50000)
print(person2.__dict__)
print(f"\n\n The number of initializations at the moment is --> {Person.number_of_person_initializated}")

# Static methods
 """
