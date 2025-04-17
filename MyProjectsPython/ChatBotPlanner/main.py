import random

HELP = """help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавляет случайную задачу на сегодня"""

random_tasks = ["Выучить Python", "Выучить SQL", "Выучить Си", "Выучить алгоритмы"]
tasks = {}
run = True

def add_todo(date, task):
    if date in tasks:  #дата есть в словаре
        tasks[date].append(task)
    else:   #даты пока нет в словаре, поэтому создаем запись
        tasks[date] = [task]
    print("Задача", task, "добавлена на дату", date)

while run:
    command = input("Введите команду: ")

    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print("-", task)
        else:
            print("Задач на эту дату нет.")
    elif command == "add":
        date = input("Введите дату для задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(random_tasks)
        add_todo("Сегодня", task)
    else:
        print("Неизвестная команда.")
        break
