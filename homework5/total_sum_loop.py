total_sum = 0

while True:
    user_input = input("Введите число или 'stop', 'end' для завершения: ").lower()

    if user_input in ["stop", "end"]:
        break

    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Пожалуйста, введите корректное число или 'stop', 'end' для завершения.")

print(f"Сумма всех введенных чисел: {total_sum}")