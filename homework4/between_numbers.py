def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число!")

a = get_integer_input("Введите первое число a: ")
b = get_integer_input("Введите второе число b: ")

if a == b:
    print("Числа равны, между ними нет других чисел.")
else:
    start = min (a, b)
    end = max(a, b)

    if start + 1 == end:
        print("Между этими числами нет целых чисел.")
    else:
        print("Целые числа между", a, "и", b, ":")
        for i in range(start + 1, end):
            print(i)