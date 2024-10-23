my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
in_x = 0
while in_x < len(my_list):
    if my_list[in_x] == 0:
        break
    elif in_x < len(my_list):
        print(my_list[in_x])
    in_x += 1
print('Вывод по поставленным условиям завершен')

