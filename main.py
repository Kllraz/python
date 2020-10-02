from random import randint
import json

# задание 1

while True:
    user_str = input("Введите текст (пустая строка - выход): ")

    if user_str == "":
        break

    with open("user_text.txt", "a", encoding="utf-8") as file:
        print(user_str, file=file)
        # file.write(f"{file}\n") # способ №2

# задание 2

with open("task_2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    lines_num = len(lines)

    for item in range(lines_num):
        line = lines[item]

        print(f"Количество строк в {item + 1}-й строке - {len(line)}")

# задание 3

with open("task_3.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    average_salary = 0

    for item in lines:
        staffs = item.split(" - ")
        average_salary += int(staffs[1])

        if int(staffs[1]) < 20000:
            print(f"У сотрудника {staffs[0]} оклад меньше 20000р")

    average_salary /= len(lines)

    print(f"Средний оклад всех сотрудников - {average_salary}р")

# задание 4

result = ""

translate = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
}

with open("task_4.txt", "r") as file:
    for line in file.readlines():
        str_list = line.split(" - ")
        result += f"{translate[str_list[0]]} - {str_list[1]}"

with open("task_4_res.txt", "w", encoding="utf-8") as file:
    file.write(result)

# задание 5

with open("task_5.txt", "a") as file:
    list_num = (f"{str(randint(0, 100))} " for item in range(10))

    file.writelines(list_num)

with open("task_5.txt", "r") as file:
    text = file.read()
    list_txt = text.split(" ")[:-1]
    list_num = map(lambda x: int(x), list_txt)
    result = sum(list_num)

print(f"Результат: {result}")

# задание 6
to_remove = ("(л)", "(пр)", "(лаб)", " -", ".")
result = {}

with open("task_6.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        subjects = line.split(":")
        lessons_num_txt = subjects[1]

        for item in to_remove:
            if item in lessons_num_txt:
                lessons_num_txt = lessons_num_txt.replace(item, "")

        lessons_num_sum = sum(map(lambda x: int(x), lessons_num_txt.split(" ")[1:]))
        result[subjects[0]] = lessons_num_sum

print(f"Результат: {result}")

# задание 7
average_profit = 0
firm_loss = {}
firm_profit = {}

with open("task_7.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        firms = line.split(" ")
        firm_name = firms[0]
        revenue = int(firms[2])
        cost = int(firms[3])

        if revenue > cost:
            profit = revenue - cost
            firm_profit[firm_name] = profit
            average_profit += profit
        else:
            firm_loss[firm_name] = revenue - cost

        list_firms = [
            firm_profit,
            {
                "average_profit": average_profit
            },
            firm_loss
        ]

print(list_firms)

with open("task_7.json", "w") as file:
    json.dump(list_firms, file)
