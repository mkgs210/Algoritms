from random import randint
import time
import matplotlib.pyplot as plt

# Сортировка прямым выбором O(n^2)
x = [i for i in range(10, 3001, 10)]
y = []

for dlin in x:

    a = [randint(0, 200) for i in range(dlin)]
    print(dlin)
    print(a)

    start_time = time.perf_counter()

    for i in range(dlin - 1):
        minim = i
        for j in range(i + 1, dlin):
            if a[j] < a[minim]:
                minim = j
        a[i], a[minim] = a[minim], a[i]

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
