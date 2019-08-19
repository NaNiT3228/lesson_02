# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

n = int(input('Введите кол-во элементов списка: '))
numbers = []
for i in range(n):
    numbers.append(random.randint(-100, 100))
# numbers = [1, 2, 3, 4, 5, 5, 4, 5, 6, 7, 8, 10, 10, -1, -2, -1]
new_numbers_1 = set(numbers)
print(list(new_numbers_1))

new_numbers_2 = []
for number in numbers:
    if numbers.count(number) == 1:
        new_numbers_2.append(number)
print(new_numbers_2)