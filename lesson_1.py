# Задание 1
print("hello world")
value_1 = 2
value_2 = 5
print(value_1, value_2)
print("Введите число: ")
number_1 = int(input())
print("Введите строку: ")
string_1 = input()
print(number_1, string_1)
# Задание 2
print("Введите секунды: ")
seconds = int(input())
minutes = seconds // 60
hours = minutes // 60
print(hours % 24, ":", minutes % 60, ":", seconds % 60 )
# Задание 3
print("Введит число: ")
n = int(input())
print(n*n+n*n*n+n*n)
# Задание 4
print("Введит число: ")
number_2 = int(input())
max = 0
while number_2 > 0:
    if number_2 % 10 > max:
        max = number_2 % 10
    number_2 = number_2 // 10
print(max)
# Задание 5
print("Введите прибыль: ")
Profit = int(input())
print("Введите издержки")
Costs = int(input())
if Profit - Costs > 0:
    print("Прибыль больше издержки")
else:
    print("Прибыль меньше издержки")
# Задание 6
print("Введите выручку: ")
Revenue = int(input())
Attitude = Profit / Revenue
print("Введите кол. сотрудников:")
n_employees = int(input())
print("Прибыль на сотрудника: ", Costs / n_employees)
# Задание 7
print("Введите a - кол. км в первый день спортсмена и b - какой результат ему нужно достигнуть: ")
a = int(input())
b = int(input())
n = 1
while a < b:
    a = a * 1.1
    n += 1
print(n)
