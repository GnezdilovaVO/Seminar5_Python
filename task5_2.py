# Напишите рекурсивную функцию sum(a, b), возвращающую 
# сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3
def sum(first_number, second_number):
    if second_number == 0 and first_number==0: return 0
    if second_number == 0: return first_number
    if first_number == 0: return second_number
    return 2 + sum(first_number - 1, second_number - 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(sum(a, b))