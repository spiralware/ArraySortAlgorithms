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
    pivot_value = array[r]  #в качестве опорного выбираем самый правый элемент
    new_pivot_pos = l
    for i in range(l, r):
        if array[i] < pivot_value:
            array[new_pivot_pos], array[i] = array[i], array[new_pivot_pos]
            new_pivot_pos = new_pivot_pos + 1
    array[new_pivot_pos], array[r] = array[r], array[new_pivot_pos]
    return new_pivot_pos

def quick_sort_impl(array, l, r):
    if l >= r:
        return

    q = partition(array, l, r)
    quick_sort_impl(array, l, q - 1)
    quick_sort_impl(array, q + 1, r)

def quick_sort(array):
    quick_sort_impl(array, 0, len(array) - 1)
