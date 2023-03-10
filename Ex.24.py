# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

i = int(input('Vvedite kol-vo kustov: '))
array_1 = []
for a in range(i):
    array_1.append(int(input('Vvedite kol-vo yagod na kuste: ')))
max = 0
for a in range(i):
    if a == 0:
        summa = array_1[a]+array_1[a+1]+array_1[i-1]
        if max < summa:
            max = summa
    elif a == i-1:
        summa = array_1[a]+array_1[a-1]+array_1[0]
        if max < summa:
            max = summa
    else:
        summa = array_1[a]+array_1[a-1]+array_1[a+1]
        if max < summa:
            max = summa
print(f'Max. kol-vo yagod, kot. mozhet sobrat modul: {max}')
