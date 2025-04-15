import random
num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку.\nВведите целое число от 1 до 100.")

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

while True:
    n = input()
    if not is_valid(n):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        n = int(n)
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок.')
            continue
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок.')
            continue
        elif n == num:
            print('Вы угадали, поздравляем!\n Хотите сыграть еще? (1 - да, все остальное - нет)')
            if int(input()) == 1:
                num = random.randint(1, 100)
                print("Введите целое число от 1 до 100.")
                continue
            else:
                break
