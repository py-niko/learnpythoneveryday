import os

while True:
    sait = input('Введите название сайта\n')

    if sait == 'Завершить':
        break

    if 'https://' in sait:
        os.system('start ' + sait)
        print('if')
    elif 'www.' in sait:
        sait = 'https://' + sait
        os.system('start ' + sait)
        print('elif')
    else:
        sait = 'https://www' + '.' + sait
        os.system('start ' + sait)
        print('else')