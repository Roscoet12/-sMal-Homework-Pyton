def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = 2000
result = is_year_leap(year)
print('Год ', year, ':', result)
