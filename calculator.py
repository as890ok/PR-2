"""
Простой калькулятор для выполнения базовых математических операций.

Поддерживаемые операции:
- Сложение (+)
- Вычитание (-)
- Умножение (*)
- Деление (/)
- Возведение в квадрат (square)
- Возведение в куб (cube)

Пример использования:
    Введите первое число: 5
    Введите операцию: +
    Введите второе число: 3
    Результат: 8.0
"""
def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание второго числа из первого."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b

def divide(a: float, b: float) -> str | float:
    """Деление первого числа на второе. Возвращает ошибку при делении на ноль."""
    return "Ошибка: деление на ноль!" if b == 0 else a / b

def square(a: float) -> float:
    """Возведение числа в квадрат."""
    return a ** 2

def cube(a: float) -> float:
    """Возведение числа в куб."""
    return a ** 3

if __name__ == "__main__":
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /, square, cube")

    a = float(input("Введите первое число: "))
    op = input("Введите операцию (+, -, *, /, square, cube): ")

    if op in ["+", "-", "*", "/"]:
        b = float(input("Введите второе число: "))
        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)
    elif op == "square":
        result = square(a)
    elif op == "cube":
        result = cube(a)
    else:
        result = "Неизвестная операция!"

    print("Результат:", result)