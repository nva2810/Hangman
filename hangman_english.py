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
        |H A N G M A N| v2020 by NVA''')


def menu():
    while True:
        choice = input('\nEnter "play" to play the game, "exit" to close: ')
        if choice == 'play':
            game()
        elif choice == 'exit':
            exit()
        else:
            print('Incorrect data. Please try again!')


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
        |             | You have {lives} lives left.''')
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
        |             | You have {lives} lives left.''')
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
        |             | You have {lives} lives left.''')
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
        |             | You have {lives} lives left.''')
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
        |             | You have {lives} lives left.''')
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
        |             | You have {lives} lives left.''')
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
        |             | You have {lives} life left.''')
        elif lives == 0:
            print(f'''          _______
          |/     |
          |     (_)   word: {random_word}
          |     _|_
          |    / | \\  !!!YOU DIED!!!
          |      |
          |     / \\
          |    /   \\
          |
        __|____________
        |             | You have no lives left.''')

    theme = dict()
    theme['animal'] = 'lion', 'giraffe', 'mouse', 'hare', 'bear', 'horse',\
                      'wolf', 'dog', 'dolphin', 'lynx', 'jackal', 'leopard',\
                      'mole', 'bat', 'moose', 'hamster', 'hyena', 'lemur',\
                      'camel', 'cheetah', 'saiga', 'porcupine', 'ferret',\
                      'antelope', 'rabbit', 'pig', 'hippopotamus', 'rat',\
                      'monkey', 'whale', 'deer', 'fox', 'ram', 'hedgehog',\
                      'gopher', 'zebra', 'snail', 'tiger', 'elephant', 'hog',\
                      'roe', 'ermine', 'raccoon', 'beaver', 'mongoose',\
                      'kangaroo', 'rhinoceros', 'fennec', 'chinchilla',\
                      'mustang', 'squirrel', 'badger', 'sheep', 'cow', 'cat'
    theme['country'] = 'china', 'india', 'usa', 'indonesia', 'pakistan',\
                       'brazil', 'nigeria', 'bangladesh', 'russia', 'mexico',\
                       'japan', 'ethiopia', 'philippines', 'drc', 'egypt',\
                       'vietnam', 'iran', 'turkey', 'germany', 'france',\
                       'uk', 'thailand', 'italy', 'tanzania', 'africa',\
                       'myanmar', 'colombia', 'kenya', 'spain', 'argentina',\
                       'algeria', 'sudan', 'ukraine', 'uganda', 'iraq',\
                       'canada', 'poland', 'morocco', 'uzbekistan',\
                       'malaysia', 'venezuela', 'afghanistan', 'peru',\
                       'angola', 'ghana', 'mozambique', 'yemen', 'nepal',\
                       'australia', 'madagascar'
    theme['sport'] = 'motorsports', 'acrobatics', 'badminton', 'basketball',\
                     'biathlon', 'billiards', 'baseball', 'boxing',\
                     'bobsleigh', 'bodybuilding', 'bowling', 'cycling',\
                     'volleyball', 'handball', 'golf', 'judo', 'esports',\
                     'curling', 'skating', 'kudo', 'swimming', 'paralympics',\
                     'poker', 'pentathlon', 'rugby', 'sledding', 'skeleton',\
                     'snowboard', 'softball', 'sumo', 'springboard',\
                     'tennis', 'triathlon', 'fencing', 'freestyle', 'soccer',\
                     'futsal', 'hockey', 'chess', 'extreme'
    theme['tv show'] = 'friends', 'scrubs', 'office', 'shameless',\
                       'chernobyl', 'brassic', 'yellowstone', 'sherlock',\
                       'poirot', 'firefly', 'anne', 'forever', 'elimination',\
                       'billions', 'futurama', 'wire', 'bron', 'daria',\
                       'simpsons', 'boys', 'dexter', 'brigade', 'rome',\
                       'dark', 'primal', 'fleabag', 'narcos', 'dokkaebi',\
                       'fargo', 'crown', 'supernatural', 'lost', 'misfits',\
                       'knick', 'fringe', 'idiot', 'mentalist', 'castle',\
                       'pacific', 'ducktales', 'merlin', 'killing',\
                       'durrells', 'harlots', 'charmed', 'homeland',\
                       'expanse', 'method', 'noragami', 'saboteur',\
                       'banshee', 'rookie'
    theme['science'] = 'logic', 'mathematics', 'statistics', 'anthropology',\
                       'history', 'sociology', 'law', 'economics',\
                       'linguistics', 'psychology', 'pedagogy', 'ethics',\
                       'aesthetics', 'journalism', 'philology',\
                       'anthropology', 'astronomy', 'biology', 'geography',\
                       'geology', 'medicine', 'meteorology', 'oceanography',\
                       'physics', 'chemistry', 'architecture',\
                       'biotechnology', 'informatics', 'cybernetics',\
                       'shipbuilding', 'aerospace', 'mechanics',\
                       'engineering', 'construction', 'energy'
    theme['hardcore'] = (theme['animal'] + theme['country']
                         + theme['sport'] + theme['tv show'] + theme['science'])
    list_of_themes = {1: 'animal', 2: 'country',
                      3: 'sport', 4: 'tv show', 5: 'science', 6: 'hardcore'}

    while True:
        user_choose = input('''
[1]. Animal
[2]. Country
[3]. Sport
[4]. TV Show
[5]. Science
[6]. Hardcore
Enter the category number: ''')
        if user_choose.isdigit() and 0 < int(user_choose) < 7:
            random_word = random.choice(theme[list_of_themes[int(user_choose)]])
            word = '-'.split() * len(random_word)
            lives = 8
            y = {''}
            print(f"\nYou'll have {lives} lives.")
            while lives:
                if random_word in ''.join(word):
                    print(f"""\n{''.join(word)} 
You guessed the word!
          _______
          |/     
          |   
          |          !!!YOU SURVIVED!!!
          |     (_)
          |     _|_/
          |    / |
          |      | 
          |     / \\
        __|____/___\\___
        |             | """)
                    menu()
                x = input(f"\n{''.join(word)}\nInput a letter: ")
                if len(x) == 1:
                    if x.isalpha() and x == x.lower():
                        if x in random_word:
                            if x in word:
                                print("You've already guessed this letter!")
                            else:
                                for n in range(len(random_word)):
                                    if random_word[n] == x:
                                        word[n] = x
                        else:
                            if x in y:
                                print("You've already entered this letter!")
                            else:
                                y.add(x)
                                lives -= 1
                                print("This letter isn't in the word!")
                                art()
                    else:
                        print('Please enter a lowercase English letter!')
                else:
                    print('You should input a single letter!')
            else:
                menu()
        else:
            print('Incorrect data. Please try again!')


menu()
