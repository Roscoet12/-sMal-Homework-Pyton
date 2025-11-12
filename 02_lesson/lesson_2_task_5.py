def month_to_season(n):
    numb = int(n)
    if numb == 1 or numb == 2 or numb == 12:
        print('Зима')
    elif 3 <= numb <= 5:
        print('Весна')
    elif 6 <= numb <= 8:
        print('Лето')
    elif 9 <= numb <= 11:
        print('Осень')
    else:
        print('Некорректный номер месяца')


month_to_season(1)
