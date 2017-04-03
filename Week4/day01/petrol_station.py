# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

class Station(object):
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self, car):
        self.gas_amount = self.gas_amount-(car.capacity-car.current)
        car.current = car.capacity


class Car(object):
    def __init__(self, current, capacity):
        self.capacity = capacity
        self.current = current



station = Station(1000)
car = Car(50, 400)
print(station.gas_amount)
print(car.capacity)
print(car.current)
print(station.refill(car))
print(car.current)
print(station.gas_amount)
