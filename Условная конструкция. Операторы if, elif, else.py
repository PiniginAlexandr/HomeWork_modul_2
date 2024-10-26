num_list = [
    int(input(f'Введите {i}-е число: '))
    for i in range(1, 3 + 1)
]
if num_list[0] == num_list[1] and num_list[0] == num_list[1] and num_list[1] == num_list[2]:
    print(f'Вывод в консоль 3: \n{num_list}')
elif num_list[0] == num_list[1] or num_list[0] == num_list[2] or num_list[1] == num_list[2]:
    print(f'Вывод в консоль 2: \n{num_list}')
else:
    print(f'Вывод в консоль 0: \n{num_list}')