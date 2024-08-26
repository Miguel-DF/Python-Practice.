class Car:
    # Constructor method to initialize the attributes of the Car class
    def __init__(self, make, model, year, color):
        self.make = make  # Brand of the car
        self.model = model  # Model of the car
        self.year = year  # Manufacturing year of the car
        self.color = color  # Color of the car

    # Method to simulate driving the car
    def drive(self):
        print("This "+ self.model + " is driving")

    # Method to simulate stopping the car
    def stop(self):
        print("This car is stopping")