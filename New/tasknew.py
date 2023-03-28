import random

user = input('Ваш вариант')
computer = random.choice(['r', 's', 'p'])

print('Компьютер выбрал:', computer)

if user == computer:
    print('Ничья')
elif user == 'r':
    if computer == 's':
        print('Игрок победил! Камень ломает ножницы!')
    else:
        print('Компьютер победил! Бумага закрывает камень!')
elif user == 'p':
    if computer == 'r':
        print('Компьютер победил! Бумага закрывает камень!')
    else:
        print('Игрок победил! Ножницы режут бумагу!')
elif user == 's':
    if computer == 'p':
        print('Игрок победил! Ножницы режут бумагу!')
    else:
        print('Компьютер победил! Камень ломает ножницы!')
