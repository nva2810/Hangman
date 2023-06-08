import random

print('''          _______
          |/     |
          |     (_)
          |     _|_
          |    / | \\
          |      |
          |     / \\
          |    /   \\
          |
        __|____________
        |H A N G M A N| v2020 by NVA
        В И С Е Л И Ц А''')


def menu():
    while True:
        choice = input('\nВведите "игра", чтобы играть, или "выход", чтобы выйти: ')
        if choice == 'игра':
            game()
        elif choice == 'выход':
            exit()
        else:
            print('Неверные данные. Пожалуйста, попробуйте еще раз!')


def game():
    def art():
        if lives == 7:
            print(f'''          _______
          |/     |
          |     (_)
          |      
          |     
          |     
          |     
          |    
          |
        __|____________
        |             | У Вас осталось {lives} жизней.''')
        elif lives == 6:
            print(f'''          _______
          |/     |
          |     (_)
          |      |
          |      | 
          |      |
          |     
          |    
          |
        __|____________
        |             | У Вас осталось {lives} жизней.''')
        elif lives == 5:
            print(f'''          _______
          |/     |
          |     (_)
          |     _|_
          |    / | 
          |      |
          |     
          |    
          |
        __|____________
        |             | У Вас осталось {lives} жизней.''')
        elif lives == 4:
            print(f'''          _______
          |/     |
          |     (_)
          |     _|_
          |    / | \\
          |      |
          |     
          |    
          |
        __|____________
        |             | У Вас осталось {lives} жизни.''')
        elif lives == 3:
            print(f'''          _______
          |/     |
          |     (_)
          |     _|_
          |    / | \\
          |      |
          |     / 
          |    
          |
        __|____________
        |             | У Вас осталось {lives} жизни.''')
        elif lives == 2:
            print(f'''          _______
          |/     |
          |     (_)
          |     _|_
          |    / | \\
          |      |
          |     / 
          |    /  
          |
        __|____________
        |             | У Вас осталось {lives} жизни.''')
        elif lives == 1:
            print(f'''          _______
          |/     |
          |     (_)
          |     _|_
          |    / | \\
          |      |
          |     / \\
          |    /  
          |
        __|____________
        |             | У Вас осталась {lives} жизнь.''')
        elif lives == 0:
            print(f'''          _______
          |/     |
          |     (_)   Слово: {random_word}
          |     _|_
          |    / | \\  !!!ВЫ УМЕРЛИ!!!
          |      |
          |     / \\
          |    /   \\
          |      
        __|____________
        |             | У Вас не осталось жизней.''')

    theme = dict()
    theme['животное'] = 'лев', 'жираф', 'мышь', 'заяц', 'медведь', 'лошадь',\
                        'волк', 'собака', 'дельфин', 'рысь', 'шакал',\
                        'леопард', 'крот', 'лось', 'хомяк', 'гиена', 'лемур',\
                        'верблюд', 'гепард', 'сайгак', 'дикобраз', 'хорек',\
                        'антилопа', 'кролик', 'свинья', 'гиппопотам',\
                        'крыса', 'обезьяна', 'кит', 'олень', 'лиса', 'баран',\
                        'еж', 'суслик', 'зебра', 'улитка', 'тигр', 'слон',\
                        'кабан', 'косуля', 'горностай', 'енот', 'бобр',\
                        'мангуст', 'кенгуру', 'носорог', 'фенек', 'шиншилла',\
                        'мустанг', 'белка', 'барсук', 'овца', 'корова',\
                        'кошка'
    theme['страна'] = 'китай', 'индия', 'сша', 'индонезия', 'пакистан',\
                      'бразилия', 'нигерия', 'бангладеш', 'россия',\
                      'мексика', 'япония', 'эфиопия', 'филиппины', 'дрк',\
                      'египет', 'вьетнам', 'иран', 'турция', 'германия',\
                      'франция', 'великобритания', 'таиланд', 'италия',\
                      'танзания', 'юар', 'мьянма', 'колумбия', 'кения',\
                      'испания', 'аргентина', 'алжир', 'судан', 'украина',\
                      'уганда', 'ирак', 'канада', 'польша', 'марокко',\
                      'узбекистан', 'малайзия', 'венесуэла', 'афганистан',\
                      'перу', 'ангола', 'гана', 'мозамбик', 'йемен', 'непал',\
                      'австралия', 'мадагаскар'
    theme['спорт'] = 'мотоспорт', 'акробатика', 'бадминтон', 'баскетбол',\
                     'биатлон', 'бильярд', 'бейсбол', 'бокс', 'бобслей',\
                     'бодибилдинг', 'боулинг', 'велоспорт', 'волейбол',\
                     'гандбол', 'гольф', 'дзюдо', 'киберспорт', 'керлинг',\
                     'коньки', 'кудо', 'плавание', 'паралимпизм', 'покер',\
                     'пятиборье', 'регби', 'сани', 'скелетон', 'сноуборд',\
                     'софтбол', 'сумо', 'трамплин', 'теннис', 'триатлон',\
                     'фехтование', 'фристайл', 'футбол', 'футзал', 'хоккей',\
                     'шахматы', 'экстрим'
    theme['сериал'] = 'друзья', 'клиника', 'офис', 'бесстыжие', 'чернобыль',\
                      'голяк', 'йеллоустоун', 'шерлок', 'пуаро', 'светлячок',\
                      'энн', 'вечность', 'ликвидация', 'миллиарды',\
                      'футурама', 'прослушка', 'мост', 'дарья', 'симпсоны',\
                      'пацаны', 'декстер', 'бригада', 'рим', 'тьма',\
                      'первобытный', 'дрянь', 'нарко', 'гоблин', 'фарго',\
                      'корона', 'сверхъестественное', 'отбросы', 'грань',\
                      'идиот', 'менталист', 'касл', 'мерлин', 'убийство',\
                      'дарреллы', 'куртизанки', 'зачарованные', 'родина',\
                      'пространство', 'метод', 'диверсант', 'банши',\
                      'новичок', 'побег'
    theme['наука'] = 'логика', 'математика', 'информатика', 'статистика',\
                     'антропология', 'история', 'социология', 'право',\
                     'политология', 'культурология', 'экономика',\
                     'лингвистика', 'психология', 'литературоведение',\
                     'искусствоведение', 'педагогика', 'этика', 'эстетика',\
                     'журналистика', 'филология', 'антропология',\
                     'астрономия', 'биология', 'ветеринария', 'география',\
                     'геология', 'медицина', 'метеорология', 'океанология',\
                     'физика', 'химия', 'архитектура', 'биотехнология',\
                     'информатика', 'кибернетика', 'кораблестроение',\
                     'космонавтика', 'материаловедение', 'механика',\
                     'системотехника', 'строительство', 'электротехника',\
                     'энергетика'
    theme['хардкор'] = (theme['животное'] + theme['страна']
                        + theme['спорт'] + theme['сериал'] + theme['наука'])
    list_of_themes = {1: 'животное', 2: 'страна',
                      3: 'спорт', 4: 'сериал', 5: 'наука', 6: 'хардкор'}

    while True:
        user_choose = input('''
[1]. Животное
[2]. Страна
[3]. Спорт
[4]. Сериал
[5]. Наука
[6]. Хардкор
Введите номер категории: ''')
        if user_choose.isdigit() and 0 < int(user_choose) < 7:
            random_word = random.choice(theme[list_of_themes[int(user_choose)]])
            word = '-'.split() * len(random_word)
            lives = 8
            y = {''}
            print(f"\nУ Вас будет {lives} жизней.")
            while lives:
                if random_word in ''.join(word):
                    print(f"""\n{''.join(word)} 
Вы угадали слово!
          _______
          |/     
          |   
          |          !!!ВЫ ВЫЖИЛИ!!!
          |     (_)
          |     _|_/
          |    / |
          |      | 
          |     / \\
        __|____/___\\___
        |             | """)
                    menu()
                x = input(f"\n{''.join(word)}\nВведите букву: ")
                if len(x) == 1:
                    if x.isalpha() and x == x.lower():
                        if x in random_word:
                            if x in word:
                                print("Вы уже угадали эту букву!")
                            else:
                                for n in range(len(random_word)):
                                    if random_word[n] == x:
                                        word[n] = x
                        else:
                            if x in y:
                                print("Вы уже вводили эту букву!")
                            else:
                                y.add(x)
                                lives -= 1
                                print("Этой буквы нет в слове!")
                                art()
                    else:
                        print('Пожалуйста, введите строчную русскую букву!')
                else:
                    print('Вы должны ввести одну букву!')
            else:
                menu()
        else:
            print('Неверные данные. Пожалуйста, попробуйте еще раз!')


menu()
