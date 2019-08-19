# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a_list = [1, 2, 3, 4]
b_list = [2, 3, 4, 5, 2]

print(a_list)

for pos in b_list:
    if pos in a_list:
        a_list.remove(pos)

print(b_list)
print(a_list)


# a = set(a_list)
# b = set(b_list)
# print('--Второй вариант--')
# c = a - b
# print(list(a))
# print(list(b))
# print(list(c))