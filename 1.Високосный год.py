year=int(input('Введите год:'))
if year%4 == 0:
    if year%100 != 0 or year%400 == 0:
        print('високосный')
    else:
        print('не високосный')
else: print('не високосный')