# Method Overriding
class vehicle:
    def move(self):
        print("Vehicle is moving")
class car(vehicle):
    def move(self):
        print("Driving on the road")
class bicycle(vehicle):
    def move(self):
        print("Pedaling on the road")
c = car()
b = bicycle()
c.move()
b.move()