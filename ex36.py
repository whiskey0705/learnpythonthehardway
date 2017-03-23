def reading():
    print('what kinds of book do you perfer?')
    books = ['红楼梦', '三国演义', '水浒传', '西游记']
    print('''
        I have four book for you, just use number 1-4 to 
        choose one, see what you get!
        ''')
    num = input('enter a number (1-4) \n')
    book = books[int(num) - 1]
    print(f'you choose {book}')

def sports():
    print('which sports do you like best?')
    sports = ['NBA', 'CBA', 'F1', 'MLB']
    print('''
        I have four choices for you, just use number 1-4 to 
        choose one, guess what you choose!
        ''')
    num = input('enter a number (1-4) \n')
    sport = sports[int(num) - 1]
    print(f'you choose {sport}')

def start():
    print('Do you want to talk about reading or sports?')
    choice = input('Make your choice \n')
    if choice == 'reading':
        reading()
    elif choice == 'sports':
        sports()
    else:
        print('Are you serious? try it again! \n')
        start()
start()