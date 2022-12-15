# # Напишите программу, которая принимает на вход вещественное число
# # и показывает сумму его цифр.(Сделать для строки)
# # *Пример:*
# # - 6782 -> 23
# # - 0,56 -> 11

n = input('Введите число: ')
chislo = n.split()
list_of_numbers = [i for i in n if i.isdigit()==True]
print(list_of_numbers)
sum = 0
for i in list_of_numbers:
    sum +=int(i)
print(sum)

# БЫЛО 
# # Вариант 1, работает:
# chislo_input = input('Введите число: ')


# print (chislo_input)
# new_chislo = chislo_input.replace(',', '0')
# new_chislo = chislo_input.replace('.', '0')
# #print (new_chislo)
# def split(x):
#     return [char for char in x]
# #print (split(new_chislo))
# chislo_for_count = split(new_chislo)
# print (chislo_for_count)
#
# summa = 0
# for i in range(0,len(chislo_for_count)):
#     chislo_for_count[i] = int (chislo_for_count[i])
#     summa += chislo_for_count[i]
# print (summa)