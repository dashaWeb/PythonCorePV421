try:
    numbers = input('Enter numbers :: ')
    list_of_numbers = [int(x) for x in numbers.split()]
    for x in list_of_numbers:
        if x < 0:
            raise ValueError('Найдено отрицательное число.')
    sum_list = sum(list_of_numbers)
    print(f'Сума чисел {sum_list}')
finally:
    print('Программа завершена.')