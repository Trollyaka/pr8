while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        print(f"Сумма: {num1 + num2}")
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")