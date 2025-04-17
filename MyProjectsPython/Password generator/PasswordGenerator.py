import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

def generate_password(s, n):
    res = random.sample(s, n)
    return res

pass_number = int(input("Введите количество паролей для генерации: "))
pass_length = int(input("Введите длину одного пароля: "))
has_numbers = input("Включает ли пароль цифры 0123456789? (да/нет) ")
has_upper = input("Включает ли пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (да/нет) ")
has_lower = input("Включает ли пароль строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет) ")
has_symbol = input("Включает ли пароль символы !#$%&*+-=?@^_? (да/нет) ")
has_ambiguous = input("Исключить неоднозначные символы il1Lo0O? (да/нет) ")

if has_numbers == 'да' or has_numbers == 'Да' or has_numbers == 'ДА':
    chars += digits
if has_upper == 'да' or has_upper == 'Да' or has_upper == 'ДА':
    chars += uppercase_letters
if has_lower == 'да' or has_lower == 'Да' or has_lower == 'ДА':
    chars += lowercase_letters
if has_symbol == 'да' or has_symbol == 'Да' or has_symbol == 'ДА':
    chars += punctuation
if has_ambiguous == 'да' or has_ambiguous == 'Да' or has_ambiguous == 'ДА':
    for c in "il1Lo0O":
        chars = chars.replace(c, "")

for _ in range(pass_number):
    res = generate_password(chars, pass_length)
    print(*res, sep='')
