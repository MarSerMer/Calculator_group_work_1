# # Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
# # *Пример:*
# # Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
# # Необходимо сложить все значения словаря и вывести  сумму на экран.

number = int(input("Please write number: "))
def func(a):
    return round((1+1/a)**a, 2)
listt = [func(x) for x in range (1,number+1)]
nums = [x for x in range (0, number)]
listt_dict = dict(zip(nums, listt))
print(listt_dict)
sum = 0
for i in listt:
    sum += i
print(sum)

#БЫЛО:
#number = int(input("Please write number: "))
#list_of_numbers = {}
# sum = 0
# for i in range(1, number+1):
#     list_of_numbers[i] = round((1+1/i)**i, 2)
#     sum += list_of_numbers[i]
# print(list_of_numbers)
# print (sum)