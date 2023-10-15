# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Child class
class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Load Capacity: {self.load_capacity} tons")

# Create a Truck object and display its information
my_truck = Truck("Ford", "F-150", 3.5)
my_truck.display_info()
