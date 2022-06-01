# Создаем класс Car
class Car:
    # создаем атрибуты класса
    name = "m3"
    make = "BMW"
    model = 2008

    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    # создаем методы класса
    def stop(self):
        print("stop car")

# Создаем объект класса Car под названием car_a
car_a = Car()
car_b = Car()

#узнать тип созданных нами объектов,
# print(type(car_a))


#car_b.start()
# car_b.stop()
# print(car_b.name)
# print(car_b.make)
# print(car_b.model)
# print(dir(car_b))


car_a.start("z3", "bmw", 2000)

print(car_a.name)
print(car_a.make)
print(car_a.model)
print(car_a.car_count)