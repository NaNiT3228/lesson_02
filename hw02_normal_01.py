# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

numbers = [2, -5, 8, 9, -25, 25, 4]
new_numbers = []

for number in numbers:
    if number > 0 and int(math.sqrt(number)) == math.sqrt(number):
        new_numbers.append(int(math.sqrt(number)))
print(numbers)
print(new_numbers)