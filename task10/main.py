# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Inpoot: 5 -> 1 0 1 1 0
# Outpoot: 2
import random

number_of_coin = 5
heads_or_tails = [random.randint(0, 1) for i in range(number_of_coin)]
print(f'{number_of_coin}  ->', *heads_or_tails, sep=' ')
heads, tails = 0, 0
for i in range(number_of_coin):
    if heads_or_tails[i] == 1:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(tails)
else:
    print(heads)