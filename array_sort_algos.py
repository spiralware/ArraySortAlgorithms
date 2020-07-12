#предполагаем, что во всех алгоритмах нужно
#отсортировать целочисленный массив по возрастанию

#сортировка пузырьком
def bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]

#сортировка вставками, которая сразу меняет местами
#соседние элементы, если следующий элемент меньше предыдущего
def insertion_sort_immediate_change(array):
    for i in range(1, len(array)):
        j = i
        while j >= 1 and array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1

#быстрая сортировка
def partition(array, l, r):
    x = array[r]  #в качестве опорного выбираем самый правый элемент
    for i in range(l, r):
        if array[i] < x:
            pass


def quick_sort(array):
    pass
