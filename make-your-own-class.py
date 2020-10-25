class Vehicle:
        def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year

        def print_info(self):
            print(f'{self.year} {self.make} {self.model} ')
        
        
        

car = Vehicle('Tesla', 'CyberTruck', 2022)

car.print_info()
