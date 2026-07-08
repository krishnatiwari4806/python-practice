class vehical :
    def start(self):
        print("Vehical started")

class car(vehical):
    def start(self):
        print("Car started")
    

class bike(vehical):
    def start(self):
        print("Bike started")

a = vehical()
b = car()
c = bike()

a.start() 
b.start()
c.start()