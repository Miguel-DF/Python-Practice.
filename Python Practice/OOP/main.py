# Importing the Car class from the car module (assuming car.py file exists)
from car import Car

# Creating an instance of the Car class with specific attributes
car_1 = Car("Chevy", "Corvette", 2021, "Blue")

# Printing the attributes of the car instance
print(car_1.make)  # Output: Chevy
print(car_1.model)  # Output: Corvette
print(car_1.year)  # Output: 2021
print(car_1.color)  # Output: Blue

# Calling the drive method on the car instance
car_1.drive()  # Output: This car is driving

# Calling the stop method on the car instance
car_1.stop()  # Output: This car is stopping