import random

def generate_list(number):
    global mas
    for i in range(number):
        mas.append(random.randint(-50, 50))
       

def sort_buble(mas):
    count = 0
    for run in range(len(mas) - 1): # количеставо проходов
            for i in range(len(mas) - 1):
                if mas[i] > mas[i + 1]:
                    count += 1
                    mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return count, mas # -> turple(count, mas)


if '__main__' == __name__:
    # создаю пустой список
    mas = []
    # прошу количество элементов нового списка
    number = int(input('Введите количество элементов списка - '))
    # вызов функции генерации чисел для списка
    generate_list(number)
    # вівод сформированого списка
    print(f'Not sorted list {mas}')
    # создание временной переменной для результата функции сортировки
    tempa = sort_buble(mas)
    # вывод count
    print(f'Count = {tempa[0]}')
    # вывод отсортированного списка
    print(tempa[1])

