my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
in_x = 0
while in_x <= len(my_list):
    if in_x < len(my_list) and my_list[in_x] >= 0:
        print(my_list[in_x])
        in_x += 1
        continue
    else:
        print('Вывод по поставленным условиям завершен')
        break
