class Car:
    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1


car_a = Car()

car_a.start("z3", "bmw", 2000)

print(car_a.name)
print(car_a.make)
print(car_a.model)
print(car_a.car_count)