print("Простой калькулятор")
print("Доступные операции: +, -, *, /, square")

# ввод чисел
a = float(input("Введите первое число: "))
op = input("Введите операцию (+, -, *, /, square): ")

# для операций с двумя числами
if op in ["+", "-", "*", "/"]:
    b = float(input("Введите второе число: "))

# выполнение
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "Ошибка: деление на ноль!"
    else:
        result = a / b
elif op == "square":
    result = a ** 2
else:
    result = "Неизвестная операция!"

print("Результат:", result)
