class Organism:
    # Class attribute indicating that all organisms are alive
    alive = True

class Animal(Organism):
    # Method to simulate the animal eating
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    # Method to simulate the dog barking
    def bark(self):
        print("This dog is barking")

# Creating an instance of the Dog class
dog = Dog()

# Checking if the dog is alive (inherited from Organism class)
print(dog.alive)  # Output: True

# Calling the eat method (inherited from Animal class)
dog.eat()  # Output: This animal is eating

# Calling the bark method (defined in Dog class)
dog.bark()  # Output: This dog is barking
