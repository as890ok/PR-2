print("Простой калькулятор")
print("Доступные операции: +, -, *, /, square")

a = float(input("Введите первое число: "))
op = input("Введите операцию (+, -, *, /, square): ")

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
else:
    result = "Неизвестная операция!"

print("Результат:", result)
