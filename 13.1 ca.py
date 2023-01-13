class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print('Moving at: ', end = '')
        self.print_speed()


myCar = Car()
myCar.set_speed(50)
myCar.print_car_speed()
