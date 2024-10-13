first_ = int(input('Ведите первое число-'))
second_ = int(input('Введите второе число-'))
third_ = int(input('Введите третье число-'))
if first_ == second_ and second_ == third_:
    print(3)
elif first_ == second_ or second_ == third_ or first_ == third_:
    print(2)
else:
    print(0)
