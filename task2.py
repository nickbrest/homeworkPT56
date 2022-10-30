# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def multip(numb):
    return [i for i in range(20, numb + 1) if i % 20 == 0 or i % 21 == 0]

print(multip(424))