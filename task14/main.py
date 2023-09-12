# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
number = 10
curent_power_of_two = 1
array_power_of_two = []
while number > curent_power_of_two:
    array_power_of_two.append(curent_power_of_two)
    curent_power_of_two *= 2
print(number, '->', *array_power_of_two, sep=' ')
