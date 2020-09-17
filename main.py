# задание 1

one = 5
two = "Тестовая переменная"
print(one, two)

user_num = int(input("Введите любое число: "))
print(f"Ваше число: {user_num}")

user_text = input("Введите любой текст: ")
print(f"Вы ввели: {user_text}")


# задание 2

user_date = int(input("Введите время в секунда: "))
hours = user_date // 3600
minutes = (user_date // 60) % 60
seconds = user_date % 60
print(f"{hours}:{minutes}:{seconds}")


# задание 3

user_number = int(input("Введите число: "))
result = user_number + int(f"{user_number}{user_number}") + int(f"{user_number}{user_number}{user_number}")
print(result)


# задание 4

user_number = int(input("Введите число: "))

max_digit = user_number % 10


while user_number > 0:
    digit = user_number % 10
    if digit > max_digit:
        max_digit = digit
    user_number //= 10

print(f"Наибольшая цифра - {max_digit}")

# задание 5

revenue = int(input("Введите значение выручки фирмы: "))
cost = int(input("Введите значение издержек фирмы: "))

if cost > revenue:
    print("Фирма работает в убыток")
else:
    profitability = (revenue / cost) * 100
    print(f"Рентабельность выручки: {profitability}%")

    staff_count = int(input("Введите количество сотрудников фирмы: "))
    revenue_per_staff = revenue / staff_count
    print(f"Прибыль фирмы в рачсете на сотрудника - {revenue_per_staff}")


# задание 6

a = int(input("Введите результат спортсмена в 1-й день: "))
b = int(input("Введите необходимый результат для вычисления дня: "))

new_result = a
day = 1

while new_result < b:
    new_result += new_result * 0.10
    day += 1

print(f"На {day}-й день спортсмен достиг результата — не менее {b} км.")
