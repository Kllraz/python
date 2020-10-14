from myExceptions import MyException, StringException


# задание 1


class Date(object):
    date_str = "09-10-2019"

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def parse_date(cls):
        """Преобразует дату из строкового формата в числовой"""

        date = cls.date_str
        list_date = list(map(int, date.split('-')))

        return list_date[0], list_date[1], list_date[2]

    @staticmethod
    def validation(day: int, month: int, year: int):
        """Проверяет дату на валидность"""

        valid_day = False
        valid_month = False
        valid_year = False

        if 0 < day <= 31:
            valid_day = True
        if 0 < month <= 12:
            valid_month = True
        if 1970 <= year >= 2100:
            valid_year = True

        return f"День - {valid_day}" \
               f"Месяц - {valid_month}" \
               f"Год - {valid_year}"

    def __str__(self):
        return self.date_str


# задание 2

def division(one_num, two_num):
    """Принимает 2 числа и выполняет их деление. Если 2-е число равно 0, то вызывается исключение"""

    if two_num == 0:
        raise MyException('Деление на нуль')

    return one_num / two_num


one = int(input("Введите число: "))
two = int(input("Введите 2-е число: "))
print(division(one_num=one, two_num=two))

# задание 3

new_list = []

while True:
    user_input = input("Введите число/строку: ")

    if user_input == 'stop':
        break

    if not user_input.isdigit():
        raise StringException("Введена строка")

    new_list.append(int(user_input))

print(f'Результат {new_list}')


# задание 4


class OfficeEquipment(object):
    def __init__(self, name='Офисная техника', quantity=1):
        """
        :param name: название
        :param quantity: количество
        """

        self.name = name
        self._quantity = quantity

    @property
    def quantity(self):
        """Возвращает кол-во"""

        return self._quantity

    def set_quantity(self, new_quantity):
        """Устанавливает переменной объекта quantity новое значение"""

        if not isinstance(new_quantity, int):
            raise StringException("Новое значение должно быть числом!")

        self._quantity = new_quantity

    def __str__(self):
        """Возвращает объект в строковом представлении"""

        return f"{self.name} - {self.quantity}"


class Printer(OfficeEquipment):
    def __init__(self, name='Принтеры', quantity=1, printer_type=False):
        """
        :param name: название
        :param quantity: количество
        :param printer_type: True - цветной, False - черно-белый
        """

        super().__init__(name, quantity)
        self.printer_type = printer_type

    def __str__(self):
        """Возвращает объект в строковом представлении"""

        return f"{super.__str__(self)}\n" \
               f"Type - {self.printer_type}"


class Scanner(OfficeEquipment):
    def __init__(self, name='Сканеры', quantity=1, dpi='1000x2000'):
        """
        :param name: название
        :param quantity: количество
        :param dpi: разрешение сканирования
        """

        name = name if name else 'Сканеры'
        super().__init__(name, quantity)
        self.dpi = dpi

    def __str__(self):
        """Возвращает объект в строковом представлении"""

        return f"{super.__str__(self)}\n" \
               f"DPI - {self.dpi}"


class Xerox(OfficeEquipment):
    def __init__(self, name='Ксероксы', quantity=1, format_paper='A4'):
        """
        :param name: название
        :param quantity: количество
        :param format_paper: формат бумаги
        """

        name = name if name else 'Ксероксы'
        super().__init__(name, quantity)
        self.format_paper = format_paper

    def __str__(self):
        """Возвращает объект в строковом представлении"""

        return f"{super.__str__(self)}\n" \
               f"format_paper - {self.format_paper}"


class Storage(object):
    def __init__(self, name='Storage'):
        """
        :param name: название склада
        """
        self.name = name
        self._storage = {}

    def add_to_storage(self, equip: OfficeEquipment, need_quantity):
        """Добавляет на склад технику"""

        name = equip.name
        quantity = equip.quantity

        if not isinstance(need_quantity, int):
            raise StringException("Количество отправляемой техники должно быть числом!")

        if equip.quantity >= need_quantity:
            self._storage[name] = need_quantity
            equip.set_quantity(quantity - need_quantity)
            print(f"{name} в количестве - {need_quantity}шт успешно добавлены на склад!")
        else:
            print(f"{name} в количестве - {need_quantity}шт нельзя добавить на склад!")

    def __str__(self):
        """Возвращает объект в строковом представлении"""

        res = ''
        for name, quat in self._storage.items():
            res += f'{name} - {quat}\n'

        return res


printers = Printer(quantity=10)
storage = Storage()

storage.add_to_storage(printers, 3)
print(printers.quantity)
print(storage)


class ComplexNumber(object):
    def __init__(self, one_num, two_num):
        """
        Создает объект комплексное число
        :param one_num: 1-е число
        :param two_num: 2-е число
        """
        self.one_num = one_num
        self.two_num = two_num

    def __add__(self, other):
        """Возвращает сумму 2х комплексных чисел"""

        if isinstance(other, ComplexNumber):
            return ComplexNumber((self.one_num + other.one_num), (self.two_num + other.two_num))

    def __mul__(self, other):
        """Возвращает произведение 2х комплексных чисел"""

        if isinstance(other, ComplexNumber):
            return ComplexNumber(((self.one_num * other.one_num) - (self.two_num * other.two_num)),
                                 ((self.one_num * other.two_num) + (self.two_num * other.one_num)))

    def __str__(self):
        """Возвращает объект в строковом представлении"""

        return f"({self.one_num} + {self.two_num}j)"


a = ComplexNumber(2, 3)
b = ComplexNumber(3, 4)

print(a + b)
print(a * b)
