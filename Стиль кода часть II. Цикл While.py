num_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list = []
ind = 0
count = len(num_list)
while count != 0:
    if num_list[ind] > 0:
        my_list.append(num_list[ind])
        count -= 1
        ind += 1
    else:
        count -= 1
        ind += 1
print(f'Список положительных чисел : {my_list}')





