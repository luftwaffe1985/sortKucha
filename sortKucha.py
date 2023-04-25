# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

from random import randint


def putInKucha(arr, n, i):
    max = i  # Инициализируем наибольший элемент как корень кучи
    left = 2 * i + 1  # Дочерний элемент слева
    right = 2 * i + 2  # Дочерний элемент справа

    # Если дочерний элемент слева > корня
    if left < n and arr[i] < arr[left]:
        max = left

    # Если дочерний элемент справа > корня
    if right < n and arr[max] < arr[right]:
        max = right

    # Если наибольшее значение изменяется
    if max != i:
        arr[i], arr[max] = arr[max], arr[i]

        # рекурсивный вызов функции putInKucha
        putInKucha(arr, n, max)


# Сортировка


def sortKucha(arr):
    n = len(arr)

    # Формирование кучи (перераспределение массива)
    for i in range(n, -1, -1):
        putInKucha(arr, n, i)

    # Достаем элементы из кучи и упорядочиваем
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # меняем корень и i-ый элемент
        putInKucha(arr, i, 0)


array = [randint(1, 100) for i in range(100)]
sortKucha(array)
print(array)
