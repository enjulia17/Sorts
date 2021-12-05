from math import ceil
from numpy import random
import time
import matplotlib.pyplot as plt
from numba import prange

# Реализация сортировки 4-слиянием
def merge_sort(lst):
    if len(lst) == 1: 
        return lst
    j = ceil(len(lst)/4)
    lst = [merge_sort(lst[i:i + j]) for i in range(0, len(lst), j)]
    return merge(lst) 

def merge(list_of_numbers):
    sorted_list = []
    while list_of_numbers:
        min_value = list_of_numbers[0][0]
        index = 0
        for element in list_of_numbers:
            if element[0] < min_value:
                min_value = element[0]
                index = list_of_numbers.index(element)
        sorted_list.append(min_value)
        list_of_numbers[index].pop(0)
        if not list_of_numbers[index]:
            list_of_numbers.remove(list_of_numbers[index])     
    return sorted_list


# Реализация сортировки на 3-куче
def heap_sort(list_of_numbers):
    for start in range(len(list_of_numbers), -1, -1):
        heap_sift(list_of_numbers, start, len(list_of_numbers) - 1) 
    for end in range(len(list_of_numbers) - 1, 0, -1): 
        list_of_numbers[end], list_of_numbers[0] = list_of_numbers[0], list_of_numbers[end]
        heap_sift(list_of_numbers, 0, end - 1)
    return list_of_numbers
  
def heap_sift(list_of_numbers, start, end):
    root = start 
    while True:
        child = root * 3 + 1
        if child > end: 
            break 
        max = child
        for k in prange(2, 4):
            current = root * 3 + k
            if current > end:
                break  
            if list_of_numbers[current] > list_of_numbers[max]:
                max = current
        if list_of_numbers[root] < list_of_numbers[max]:
            list_of_numbers[root], list_of_numbers[max] = list_of_numbers[max], list_of_numbers[root]
            root = max
        else:
            break

# Функция для работы с данными (выбор количества элементов в исходном массиве, нижней и верхней границ для значений элементов массива, способа заполнения массива)
def experimental_data():
    n = int(input('Quantity of elements in array: ')) 
    q = int(input('Lower bound: ')) 
    w = int(input('Upper bound: '))
    array_filling_option = int(input('Choose the way to fill the array: ')) 
    if array_filling_option ==  1: # псевдослучайное
        array_a = random.randint(q, w + 1, size = n).tolist()
    elif array_filling_option ==  2: # автоматическое по неубыванию
        array_a = random.randint(q, w + 1, size = n).tolist()
        array_a.sort()
    elif array_filling_option ==  3: # автоматическое по невозрастанию
        array_a = random.randint(q, w + 1, size = n).tolist()
        array_a.sort(reverse = True)    
    return array_a

# Функция для тестирования работоспособности программы (выводит отсортированный список и время работы двух алгоритмов)
def testing_1():
    list_of_nums = experimental_data()
    start_time_A = time.time()
    result_A = merge_sort(list_of_nums)
    end_time_A = time.time()
    print(result_A)
    print("Running time of algorithm A is {} seconds".format(end_time_A - start_time_A))

    start_time_B = time.time()
    result_B = heap_sort(list_of_nums)
    end_time_B = time.time()
    print(result_B)
    print("Running time of algorithm B is {} seconds".format(end_time_B - start_time_B))

# Функция для проведения экспериментов (возвращает время работы обоих алгоритмов)
def testing(lst):
    start_time_A = time.time()
    merge_sort(lst)
    end_time_A = time.time()
    running_time_A = end_time_A - start_time_A

    start_time_B = time.time()
    heap_sort(lst)
    end_time_B = time.time()
    running_time_B = end_time_B - start_time_B

    return running_time_A, running_time_B

# Следующие три функции для проведения первого эксперимента (с разным количеством элементов в массиве, рисует графики зависимости времени работы алгоритмов от размера массива)
def experiment_1_with_pseudo_random(): 
    q = 1
    w = pow(10, 9)
    A_coordinate_y = []
    B_coordinate_y = []
    coordinate_x = []
    array_a = None
    k = pow(10, 6)
    step = pow(10, 4)
    for n in prange(1, k + 1, step):
        coordinate_x.append(n)
        array_a = random.randint(q, w + 1, size = n).tolist()
        T_a, T_b = testing(array_a)
        A_coordinate_y.append(T_a)
        B_coordinate_y.append(T_b)
    plt.style.use('seaborn-poster') 
    x = coordinate_x
    y_a = A_coordinate_y
    y_b = B_coordinate_y
    plt.figure(1)
    plt.plot(x, y_a, 'r')
    plt.plot(x, y_b, 'g')
    plt.xlabel('Array size')
    plt.ylabel('Runtime')
    plt.title('First experiment results')

def experiment_1_with_automatic_increasing():
    q = 1
    w = pow(10, 9)
    A_coordinate_y = []
    B_coordinate_y = []
    coordinate_x = []
    array_a = None
    k = pow(10, 6)
    step = pow(10, 4)
    for n in prange(1, k + 1, step):
        coordinate_x.append(n)
        array_a = random.randint(q, w + 1, size = n).tolist()
        array_a.sort()
        T_a, T_b = testing(array_a)
        A_coordinate_y.append(T_a)
        B_coordinate_y.append(T_b)
    plt.style.use('seaborn-poster') 
    x = coordinate_x
    y_a = A_coordinate_y
    y_b = B_coordinate_y
    plt.figure(2)
    plt.plot(x, y_a, 'r')
    plt.plot(x, y_b, 'g')
    plt.xlabel('Array size')
    plt.ylabel('Runtime')
    plt.title('First experiment results')

def experiment_1_with_automatic_decreasing():
    q = 1
    w = pow(10, 9)
    A_coordinate_y = []
    B_coordinate_y = []
    coordinate_x = []
    array_a = None
    k = pow(10, 6)
    step = pow(10, 4)
    for n in prange(1, k + 1, step):
        coordinate_x.append(n)
        array_a = random.randint(q, w + 1, size = n).tolist()
        array_a.sort(reverse = True) 
        T_a, T_b = testing(array_a)
        A_coordinate_y.append(T_a)
        B_coordinate_y.append(T_b)
    plt.style.use('seaborn-poster') 
    x = coordinate_x
    y_a = A_coordinate_y
    y_b = B_coordinate_y
    plt.figure(3)
    plt.plot(x, y_a, 'r')
    plt.plot(x, y_b, 'g')
    plt.xlabel('Array size')
    plt.ylabel('Runtime')
    plt.title('First experiment results')


# Следующие три функции для проведения второго эксперимента (с разными верхними границами для значений элементов массива, рисует графики зависимости времени работы алгоритмов от верхней границы значений элементов массива)
def experiment_2_with_pseudo_random():
    q = 1
    n = pow(10, 6)
    A_coordinate_y = []
    B_coordinate_y = []
    coordinate_x = []
    array_a = None
    for w in prange(1, 101, 1):
        coordinate_x.append(w)
        array_a = random.randint(q, w + 1, size = n).tolist()
        T_a, T_b = testing(array_a)
        A_coordinate_y.append(T_a)
        B_coordinate_y.append(T_b)
    plt.style.use('seaborn-poster') 
    x = coordinate_x
    y_a = A_coordinate_y
    y_b = B_coordinate_y
    plt.figure(4)
    plt.plot(x, y_a, 'r')
    plt.plot(x, y_b, 'g')
    plt.xlabel('Upper bound of values')
    plt.ylabel('Runtime')
    plt.title('Second experiment results')

def experiment_2_with_automatic_increasing():
    q = 1
    n = pow(10, 6)
    A_coordinate_y = []
    B_coordinate_y = []
    coordinate_x = []
    array_a = None
    for w in prange(1, 101, 1):
        coordinate_x.append(w)
        array_a = random.randint(q, w + 1, size = n).tolist()
        array_a.sort()
        T_a, T_b = testing(array_a)
        A_coordinate_y.append(T_a)
        B_coordinate_y.append(T_b)
    plt.style.use('seaborn-poster') 
    x = coordinate_x
    y_a = A_coordinate_y
    y_b = B_coordinate_y
    plt.figure(5)
    plt.plot(x, y_a, 'r')
    plt.plot(x, y_b, 'g')
    plt.xlabel('Upper bound of values')
    plt.ylabel('Runtime')
    plt.title('Second experiment results')

def experiment_2_with_automatic_decreasing():
    q = 1
    n = pow(10, 6)
    A_coordinate_y = []
    B_coordinate_y = []
    coordinate_x = []
    array_a = None
    for w in prange(1, 101, 1):
        coordinate_x.append(w)
        array_a = random.randint(q, w + 1, size = n).tolist()
        array_a.sort(reverse = True) 
        T_a, T_b = testing(array_a)
        A_coordinate_y.append(T_a)
        B_coordinate_y.append(T_b)
    plt.style.use('seaborn-poster') 
    x = coordinate_x
    y_a = A_coordinate_y
    y_b = B_coordinate_y
    plt.figure(6)
    plt.plot(x, y_a, 'r')
    plt.plot(x, y_b, 'g')
    plt.xlabel('Upper bound of values')
    plt.ylabel('Runtime')
    plt.title('Second experiment results')


if __name__ == '__main__':
    # Проверка, что программа работает корректно
    testing_1()
    
    # Проведение экспериментов    
    experiment_1_with_pseudo_random()
    experiment_1_with_automatic_increasing()
    experiment_1_with_automatic_decreasing()

    experiment_2_with_pseudo_random()
    experiment_2_with_automatic_increasing()
    experiment_2_with_automatic_decreasing()

    plt.show()
