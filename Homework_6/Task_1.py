# 1 Написать программу вычисления арифметического выражения,
# заданного строкой.
# Используйте операции +, -, /, *, приоритет операций стандартный
# Пример:
# 2 + 2 => 4
# 1 + 2 * 3 => 7
# 1 - 2 * 3 => -5

start_string = '1 - 2 * 3'
start_string = start_string.split()
print (start_string)


while len(start_string) > 1:
    while '/' in start_string or '*' in start_string:
        if start_string.count('/')>0 and start_string.count('*')>0:
            if start_string.index('/') > start_string.index('*'):
                i = start_string.index('*')
                temp = int(start_string[i - 1]) * int(start_string[i + 1])
                start_string[i - 1] = str(temp)
                start_string.pop(i + 1)
                start_string.pop(i)
                print(start_string)
                print(len(start_string))
            else:
                i = start_string.index('/')
                temp = int(start_string[i - 1]) / int(start_string[i + 1])
                start_string[i - 1] = str(temp)
                start_string.pop(i + 1)
                start_string.pop(i)
                print(start_string)
                print(len(start_string))
                print('')
        elif start_string.count('/')>0:
            i = start_string.index('/')
            temp = int(int(start_string[i - 1]) / int(start_string[i + 1]))
            start_string[i - 1] = str(temp)
            start_string.pop(i + 1)
            start_string.pop(i)
            print(start_string)
            print(len(start_string))
            print('')
        elif start_string.count('*')>0:
            i = start_string.index('*')
            temp = int(start_string[i - 1]) * int(start_string[i + 1])
            start_string[i - 1] = str(temp)
            start_string.pop(i + 1)
            start_string.pop(i)
            print(start_string)
            print(len(start_string))
            print('')
    if '+' in start_string:
        i = start_string.index('+')
        temp = int(start_string[i - 1]) + int(start_string[i + 1])
        start_string[i - 1] = str(temp)
        start_string.pop(i + 1)
        start_string.pop(i)
        print(start_string)
        print(len(start_string))
        print('')
    if '-' in start_string:
        i = start_string.index('-')
        temp = int(start_string[i - 1]) - int(start_string[i + 1])
        start_string[i - 1] = str(temp)
        start_string.pop(i + 1)
        start_string.pop(i)
        print(start_string)
        print(len(start_string))
        print('')



print ('FINAL ANSWER: ', start_string)
