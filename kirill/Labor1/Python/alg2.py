from random import randint
import time
import matplotlib.pyplot as plt

# Сортировка вставками O(n^2)
x = [i for i in range(10, 3001, 10)]
y = []

for dlin in x:

    a = [randint(0, 200) for i in range(dlin)]
    print(dlin)
    print(a)

    start_time = time.perf_counter()

    for i in range(1, dlin):
        temp = a[i]
        j = i
        while (j - 1 >= 0) and (a[j - 1] > temp):
            a[j - 1], a[j] = a[j], a[j - 1]
            j = j - 1
        a[j] = temp

    print(a)
    sek = time.perf_counter() - start_time
    print(sek, "seconds")
    y.append(sek)
    print()

plt.title("Зависимость времени от размера массива")  # заголовок
plt.xlabel("Размер массива")  # ось абсцисс
plt.ylabel("Время")  # ось ординат
plt.grid()  # включение отображение сетки
plt.plot(x, y)  # построение графика
plt.show()
