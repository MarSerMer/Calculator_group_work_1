# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import math

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Please enter N: "))

# СТАЛО:
numbers = [math.factorial(i) for i in range(1,number+1)]
print(' ')
print(numbers)

# БЫЛО:
# j = 1
# for i in range(1,number+1):
#     print (math.factorial(j), end=(' '))
#     j +=1
