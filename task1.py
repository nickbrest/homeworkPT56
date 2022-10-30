# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.

from random import randint

def up_elem(numb):
    random_numbs = [randint(1, 100) for _ in range(numb)]
    print(random_numbs)
    # return [random_numbs[i] for i in range(1, len(random_numbs)) if random_numbs[i] > random_numbs[i-1]]
    return [j for i, j in zip(random_numbs, random_numbs[1:]) if j > i]

print(up_elem(10))