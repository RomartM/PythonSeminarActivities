#Define Class

class House:

    floor_size = 0
    no_of_floors = 0
    no_of_doors = 0

    def __init__(self, floor_size, no_of_floors, no_of_doors):
        self.floor_size = floor_size
        self.no_of_floors = no_of_floors
        self.no_of_doors = no_of_doors

    def lightOpen(self):
        print("Light Opened")

    def ovenOpen(self):
        print("Oven Opened")

    def switchOn(self):
        self.lightOpen()
        self.ovenOpen()

class TownHouse(House):

    def __init__(self, floor_size, no_of_floors, no_of_doors):
        self.no_of_floors = no_of_floors
        self.no_of_doors = no_of_floors
        House.__init__(self, floor_size, self.no_of_doors, self.no_of_floors)

    def display(self):
        print("House Properties\nFloor Size: {}\nNo. of Floors {}\nNo. of doors {}".format(self.floor_size, self.no_of_floors, self.no_of_doors))


town_house = TownHouse(300, 4, 2)

town_house.display()
town_house.switchOn()