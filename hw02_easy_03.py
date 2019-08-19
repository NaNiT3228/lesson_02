# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [1, 5, 10, 24, 53, 2, 44, 2312]
new_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        new_numbers.append(numbers[i] / 4)
    else:
        new_numbers.append(numbers[i] * 2)
print(new_numbers)