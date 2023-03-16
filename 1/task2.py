lst = []
for _ in range(3):
    data = input("Введите дату: ")
    task = input("Введите задачу: ")
    lst.append(f'{data} {task}')
for i in lst:
    print(i)
