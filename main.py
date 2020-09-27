from sys import argv
from functools import reduce
from itertools import cycle, count


# задание 1

def payroll_accounting(output_in_hours,
                       rate_per_hour,
                       prize):
    """
    Функция расчета заработной платы сотрудника
    :param output_in_hours: выработка в часах
    :param rate_per_hour: ставка в час
    :param prize: премия
    :return: заработную плату сотрудника
    """
    return (output_in_hours * rate_per_hour) + prize


result = payroll_accounting(output_in_hours=int(argv[1]), rate_per_hour=int(argv[2]), prize=int(argv[3]))
print(f"Результат: {result}")

# задание 2

input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
output_list = [input_list[item] for item in range(len(input_list)) if item and input_list[item] > input_list[item - 1]]

print(f"Результат: {output_list}")

# задание 3

out_list = [item for item in range(20, 240) if item % 20 == 0 or item % 21 == 0]
print(f"Результат: {out_list}")

# задание 4

input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
output_list = [item for item in input_list if input_list.count(item) == 1]
print(f"Результат: {output_list}")

# задание 5

input_list = [item for item in range(100, 1001) if item % 2 == 0]
output_list = reduce(lambda x, y: x * y, input_list)

print(f"Результат: {output_list}")

# задание 6 a

for item in count(3):
    if item == 10:
        break

    print(item)

# задание 6 b

my_list = ["abc", 5, 4.54, True]
c = 0

for item in cycle(my_list):
    if c == 10:
        break

    print(item)
    c += 1


def fact(n):
    """
    Функция возвращает генератор. Отвечает за получение факториала числа n
    :param n: число
    :return: генератор
    """
    for el in range(1, n + 1):
        input_list = [i for i in range(1, el + 1)]
        out = reduce(lambda x, y: x * y, input_list)

        yield out


for item in fact(4):
    print(item)
