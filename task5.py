HELP = """help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выйти"""

today, tomorrow, other = [], [], []

while True:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print('Сегодня:', *today)
        print('Завтра:', *tomorrow)
        print('Другое:', *other)
    elif command == "add":
        task = input("Введите название задачи: ")
        a = input("Введите дату: ")
        if a == 'Сегодня':
            today.append(task)
        elif a == 'Завтра':
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        print("До свидания!")
        break
