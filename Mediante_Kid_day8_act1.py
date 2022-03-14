#Define Class

class Car:

    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

    def display(self):
        print("Car Properties: \nColor:{}\nModel:{}\nManufacturer:{}\n".format(self.color, self.model, self.manufacturer))

# Init Class

car_1 = Car("Red", "UX Hybrid", "Lexus")
car_2 = Car("Black", "S90", "Volvo")
car_3 = Car("Ocean Blue", "HSE", "Range Rover")


# Display Properties

car_1.display()
car_2.display()
car_3.display()