# 1. Написать свой генератор последовательностей, свой тернарный оператор
# 2. Написать свой декоратор
# 3. Выполнить задание уровня ultra-light
# 4. Написать декоратор, замеряющий время выполнение декорируемой функции.
# 5. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
# (создание объектов оформить в виде функций)

task_list = ['Задание №1', 'Задание №2','Задание №4', 'Задание №5']

# Задание №1
# Написать свой генератор последовательностей, свой тернарный оператор

N = 20
list_math_sequence = [i+(i**2) for i in range (1, N+1) if i%2 != 0] #математическая последовательность из нечетных числе
print(task_list[0]+' - ' + 'генератор последовательностей на основе тернарного оператора:\n',list_math_sequence, '\n')

# Задание №2
# Написать свой декоратор

def lesson_decor(f):
    def wrapper(*args, **kwargs):
        print(task_list[1]+':')
        print('=============================================')
        f(*args, **kwargs)
        print('=============================================','\n')
    return wrapper

@lesson_decor
def math_sequence():
    N = 20
    list_math_sequence = [i + (i ** 2) for i in range(1, N + 1) if i % 2 != 0]
    print(list_math_sequence)

math_sequence()

# Задание №4
# Написать декоратор, замеряющий время выполнение декорируемой функции.

import time

def lesson_decor(f):
    def wrapper(*args, **kwargs):
        print(task_list[2]+':')
        print('=============================================')
        f(*args, **kwargs)
        print('=============================================')
#
    return wrapper
@lesson_decor
def math_sequence():
    N = 20
    list_math_sequence = [i + (i ** 2) for i in range(1, N + 1) if i % 2 != 0]
    print(list_math_sequence)

math_sequence()

start = time.time()
lesson_decor(math_sequence)
print('Время выполнения функции декоратора {} секунд'.format(time.time() - start), '\n')

# Задание №4 (вариант II)
# def lesson_decor(f):
#     start = time.time()
#     def wrapper(*args, **kwargs):
#         print(task_list[2]+':')
#         print('=============================================')
#         f(*args, **kwargs)
#         print('=============================================')
#         print('Время выполнения функции декоратора {} секунд'.format(time.time() - start))
#
#     return wrapper
# @lesson_decor
# def math_sequence():
#     N = 20
#     list_math_sequence = [i + (i ** 2) for i in range(1, N + 1) if i % 2 != 0]
#     print(list_math_sequence)
#
# math_sequence()

# Задание №5
# Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
# (создание объектов оформить в виде функций)

print(task_list[3]+':')
# функция создание списка простым методом
def list_number(N):
    list_natur_num = []
    for i in range (1,N+1):
        list_natur_num.append(i)
    return (list_natur_num)

start = time.time()
list_number(1000000)
print('Время создания списка простым методом {} секунд'.format(time.time() - start))


#функция создания списка через генератор последовательностей
def list_gen(n):
    list_num_gen = [i for i in range (1, n+1)]

start = time.time()
list_gen(1000000)
print('Время создания списка c помощью генератора последовательностей {} секунд'.format(time.time() - start))
