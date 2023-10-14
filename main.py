import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

unique_el = list(set(lst))              # создаем список с уникальными элементами
one_hot = {el: [] for el in unique_el}  # создаем словарь, значения - пустые списки, ключи - уникальные элементы

for el1 in lst:
    for el2 in unique_el:
        if el1 == el2:
            one_hot[el2] += ['True']    # если елемент из списка совпал с уникальным элементом,
        else:                           # добаляем в словарь 'True', используя уникальный элемент, как ключ
            one_hot[el2] += ['False']   # в противном случае, добавляем 'False'

res = pd.DataFrame(one_hot)
print(res)
