import random
word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ', 
'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА', 'СКОВОРОДА', 
'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК', 
'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН', 
'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН', 
'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР', 
'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК', 
'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА', 
'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ', 'ДИСК']

def get_word():
    n = random.randint(0, len(word_list) - 1)
    res = word_list[n].upper()
    return res

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = ['_'] * len(word)  # список, содержащий символы _ на каждую букву задуманного слова
    guessed = False                # сигнальная метка
    guessed_letters = []           # список уже названных букв
    guessed_words = []             # список уже названных слов
    tries = 6                      # количество попыток

    print('Давайте играть в угадайку слов! ')
    print(*word_completion, sep = '')
    print(display_hangman(tries))
    
    while tries > 0:
        s = input('Если уже угадали слово, напишите его. Либо напишите букву, которая может быть в этом слове.\n').upper()
        if len(s) == 1 and s.isalpha():
            if s in guessed_letters:
                print('Эту букву вы уже называли. ')
                print(*word_completion, sep='')
            elif s in word:
                for i in range(len(word)):
                    if s == word[i]:
                        word_completion[i] = s
                guessed_letters.append(s)
                if word_completion == list(word):
                    print(f'Поздравляю! Вы угадали слово: {word}')
                    guessed = True
                    break
                else:
                    print('Поздравляю! Вы угадали букву!')
                    print(*word_completion, sep='')
                    tries -= 1
            else:
                print('Простите, но такой буквы в этом слове нет')
                guessed_letters.append(s)
                print(*word_completion, sep='')
                tries -= 1
        elif s.isalpha():
            if len(s) == len(word):
                if s == word:
                    print(f'Поздравляю! Вы угадали слово: {word}')
                    guessed = True
                    break
                else:
                    print('Простите, но вы не угадали слово.')
                    print(*word_completion, sep='')
                    tries -= 1
            else:
                print('Вы не угадали слово. (!) Обратите внимание на длину слова.')
                print(*word_completion, sep='')
                tries -= 1
        else:
            print('Что это вы написали?')
            print(*word_completion, sep='')
            tries -= 1
        if guessed == False:
            print(display_hangman(tries))
    if tries == 0 and guessed == False:
        print(f'Мне очень жаль, вы проиграли. Это было слово {word}')

play(get_word())