print("Простой калькулятор")
print("Доступные операции: +, -, *, /, square, cube")

a = float(input("Введите первое число: "))
op = input("Введите операцию (+, -, *, /, square, cube): ")

if op in ["+", "-", "*", "/"]:
    b = float(input("Введите второе число: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = "Ошибка: деление на ноль!" if b == 0 else a / b
elif op == "square":
    result = a ** 2
elif op == "cube":
    result = a ** 3
else:
    result = "Неизвестная операция!"

print("Результат:", result)
