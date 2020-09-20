# задание 1

my_list = [123, 1.63, "abc", None, True]

for item in my_list:
    print(f"Тип для '{item}': ", type(item))

# задание 2

my_list = []

while True:
    user_input = input("Введите значение следующего элемента или 'exit' для выхода: ")

    if user_input == 'exit':
        break

    my_list.append(user_input)


for item in range(0, len(my_list), 2):
    if item + 1 < len(my_list):
        my_list[item], my_list[item + 1] = my_list[item + 1], my_list[item]

print(my_list)

# задание 3

user_month = int(input("Введите номер месяца: "))

month_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето",  "Осень", "Осень", "Осень", "Зима"]
month_dict = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима",
}

print(f"Вариант с list: {month_list[user_month - 1]}\n"
      f"Вариант с dict: {month_dict[user_month]}")

# 2-й вариант с dict

# month_dict = {
#     "Зима": (1, 2, 12),
#     "Весна": (3, 4, 5),
#     "Лето": (6, 7, 8),
#     "Осень": (9, 10, 11),
# }
#
#
# for key in month_dict.keys():
#     if user_month in month_dict[key]:
#         print(key)

# задание 4

user_str = input("Введите слова, разделенные пробелами: ").split(" ")

for item in range(len(user_str)):
    txt = user_str[item]
    print(f"{item + 1}. {txt[:10]}")

# задание 5

my_list = [7, 5, 3, 3, 2]

user_num = int(input("Введите новый элемент рейтинга: "))

if user_num in my_list:
    index_of_num = my_list.index(user_num)
    my_list.insert(index_of_num + 1, user_num)
else:
    my_list.append(user_num)
print(my_list)

# задание 6

list_goods = []
article_number = 0

while True:
    user_txt = input("Введите название товара или 'exit' для выхода: ")

    if user_txt == 'exit':
        break

    cost = int(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения: ")
    article_number += 1

    new_tuple = (
        article_number, {
            "название": user_txt,
            "цена": cost,
            "количество": count,
            "ед": unit,
        }
    )

    list_goods.append(new_tuple)

print("Структура 'ТОВАРЫ':", list_goods)

product_analytics = {
    "название": [],
    "цена": [],
    "количество": [],
    "ед": []
}

for _, goods in list_goods:
    for key, value in goods.items():
        product_analytics[key].append(value)

print(product_analytics)
