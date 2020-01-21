class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.year = 1991

    def print_info(self):
        return self.model

vehical = Car("Toyoda", "z-series")
print(vehical.print_info())