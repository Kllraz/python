# задание 1


def division(num_1, num_2):
    """
    Функция деления чисел

    :param num_1: 1-е число
    :param num_2: 2-е число
    :return: результат деления, или ошибку, если деление на 0
    """

    if not num_2:
        return "Деление на 0!"

    return num_1 / num_2


number_1 = int(input("Введите 1-е число: "))
number_2 = int(input("Введите 2-е число: "))

print(f"{division(number_1, number_2)}")


# задане 2


def make_profile(name,
                 surname,
                 date_of_birth,
                 city,
                 email,
                 phone_number):
    """
    Функция, создаюзая анкету пользователя

    :param name: имя пользователя
    :param surname: фамилия пользователя
    :param date_of_birth: дата рождения пользователя
    :param city: город проживания пользователя
    :param email: почта пользователя
    :param phone_number: телефон поьзователя
    :return: анкету пользователя
    """

    print(f"Имя: {name}, "
          f"Фамилия: {surname}, "
          f"Дата рождения: {date_of_birth}, "
          f"Город проживания: {city}, "
          f"Email: {email}, "
          f"Номер телефона: {phone_number}")


make_profile(name="Иван",
             surname="Журавлев",
             date_of_birth="07.03.1999",
             city="Санкт-Петербург",
             email="i.zhuravlev@mail.ru",
             phone_number="+79818675566")


# задани 3

def my_func(arg_1, arg_2, arg_3):
    """
    Функция, возвращающая сумму 2-х наибольших аргументов из 3-х чисел
    :param arg_1: 1-е число
    :param arg_2: 2-е число
    :param arg_3: 3-е число
    :return: сумма 2-х наибольших аргументов
    """

    sorted_numbers = sorted((arg_1, arg_2, arg_3), reverse=True)

    return sorted_numbers[0] + sorted_numbers[1]


print(my_func(3, 2, 44))


# задание 4

def my_func(x, y):
    """
    Фунция, возводящая число в степень 2-мя способами
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: число в степени y
    """
    result_1 = x ** y
    result_2 = 1

    for _ in range(abs(y)):
        result_2 /= x

    return f"Результат 1: {result_1}\n" \
           f"Результат 2: {result_2}"


print(my_func(5, -2))

# задание 5

result = 0

while True:
    user_txt = input("Введите строку чисел, разеленную пробелами или введите 'exit' для выхода: ")
    user_txt_list = user_txt.split(" ")

    if user_txt == "exit":
        break

    if "exit" in user_txt_list:
        user_txt_list.remove("exit")

        user_numbers_list = map(lambda x: int(x), user_txt_list)
        result += sum(user_numbers_list)

        break

    user_numbers_list = map(lambda x: int(x), user_txt_list)
    result += sum(user_numbers_list)

    print(f"Результат: {result}")

print(f"Результат: {result}")


def int_func(text: str):
    """
    Функция, возвращающая строку, но с прописной первой буквой
    :param text: строка
    :return: стрка с прописной 1-й буквой
    """
    return f"{text[0].upper()}{text[1:]}"


print(int_func("abc"))

user_txt = input("Введите слова, разделенные пробелом: ")
result = []

for item in user_txt.split(" "):
    modify_str = int_func(item)
    result.append(modify_str)

result_txt = " ".join(result)

print(f"Результат: {result_txt}")
