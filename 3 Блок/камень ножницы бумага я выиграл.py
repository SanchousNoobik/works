a=input()
b=input()
if a==b:
    print('ничья, я выиграл')
else:
    if a=='бумага':
        if b=='камень':
            print('я выйграл')
        else:
            print('ты проиграл')
    if a=='камень':
        if b=='бумага':
            print('ты проиграл')
        else:
            print('я выиграл')
    if a=='ножницы':
        if b=='бумага':
            print('я выиграл')
        else:
            print('ты проиграл')

