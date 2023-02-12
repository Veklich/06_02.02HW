# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


n = int(input('Vvedite dlinu PERVOGO nabora: '))
m = int(input('Vvedite dlinu VTOROGO nabora: '))
set_n = set()
set_m = set()
for i in range(n):
    set_n.add(int(input('Vvodite znacheniya PERVOGO nabora: ')))
print(sorted(set_n))
print()
for i in range(m):
    set_m.add(int(input('Vvodite znacheniya VTOROGO nabora: ')))
print(sorted(set_m))
set_n.update(set_m)
print(sorted(set_n))