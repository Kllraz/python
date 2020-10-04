from time import sleep

# задание 1


class TrafficLight(object):
    modes = {
        1: (
            "Красный", 7
        ),
        2: (
            "Желтый", 2
        ),
        3: (
            "Зеленый", 10
        )
    }

    def __init__(self, color):
        self.__color = color

    def _running(self):
        mode = 1

        for item in self.modes.keys():
            if self.__color in self.modes[item][0]:
                mode = item

        last_mode = mode - 1

        while True:
            # раскоментировать, чтобы получить возможность выхода из цикла
            # user_input = input("Введите ДА, чтобы продолжить: ")
            # if user_input.lower() != "да":
            #     break

            if last_mode != mode - 1:
                print("Ошибка в порядке рижимов!")
                break

            print(self.modes[mode][0])
            sleep(self.modes[mode][1])
            mode = 1 if mode == 3 else + 1


svet = TrafficLight("Зеленый")
svet._running()


# задание 2


class Road(object):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_mass(self, weight_per_one_meter=25, thickness=1):
        result = self.__length * self.__width * weight_per_one_meter * thickness

        return result / 1000


new_road = Road(20, 5000)
res = new_road.get_mass(25, 5)
print(f"Результат - {res}т")


# задание3


class Worker(object):
    def __init__(self, name, surname, position, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        income = self._income["wage"] + self._income["bonus"]

        return income


pos = Position("Борис", "Лебедев", "Бухгалтер", {"wage": 35000, "bonus": 5500})
print(f"Имя - {pos.name}\n"
      f"Фамилия - {pos.surname}\n"
      f"Должность - {pos.position}\n"
      f"Доход - {pos.get_total_income()}\n"
      f"Полное имя - {pos.get_full_name()}\n")

# задание 4


class Car(object):
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость машины {self.name} - {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} превысила скорость!")
        else:
            print(f"Скорость машины {self.name} - {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} превысила скорость!")
        else:
            print(f"Скорость машины {self.name} - {self.speed}")


class PoliceCar(Car):
    pass


town_car = TownCar(70, "white", "TownCar", False)
sport_car = SportCar(130, "orange", "SportCar", False)
work_car = WorkCar(50, "red", "WorkCar", False)
police_car = PoliceCar(80, "blue", "PoliceCar", True)

print(f"Цвет town_car - {town_car.color}\n"
      f"Скорость town_car - {town_car.speed}\n"
      f"Имя town_car - {town_car.name}\n"
      f"Is_police town_car - {town_car.is_police}")
town_car.show_speed()

print(f"Цвет sport_car - {sport_car.color}\n"
      f"Скорость sport_car - {sport_car.speed}\n"
      f"Имя sport_car - {sport_car.name}\n"
      f"Is_police sport_car - {sport_car.is_police}")
sport_car.show_speed()

print(f"Цвет work_car - {work_car.color}\n"
      f"Скорость work_car - {work_car.speed}\n"
      f"Имя work_car - {work_car.name}\n"
      f"Is_police work_car - {work_car.is_police}")
work_car.show_speed()

print(f"Цвет police_car - {police_car.color}\n"
      f"Скорость police_car - {police_car.speed}\n"
      f"Имя police_car - {police_car.name}\n"
      f"Is_police police_car - {police_car.is_police}")
police_car.show_speed()


# задание 5


class Stationery(object):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки - {self.title}")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки - Ручка")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки - Карандаш")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки - маркер")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()
