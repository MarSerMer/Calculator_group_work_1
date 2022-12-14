
from datetime import datetime as dt
# a - первое число, которое вводит пользователь
# b - знак, который вводит пользователь
# c - второе число, которое вводит пользователь
# d - результат, который посчитал(=вернул) один из вычислительных модулей

def logger (a,b,c,d):
    with open ('List_of_all_countings.txt', 'a') as file:
        time = dt.now().strftime('%D  %H:%M')
        data = str(a) + ' ' + str (b) + ' ' + str (c) + ' = ' + str(d)
        file.write('{}\n{}\n'.format(time,data))
        print ('{}\n{}\n'.format(time,data))

logger (3,'-',4,-1)
