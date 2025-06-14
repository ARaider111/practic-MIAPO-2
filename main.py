
def Addition():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a} + {b} = {a + b}")

def Subtraction():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a} - {b} = {a - b}")

def Multiplication():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a} * {b} = {a * b}")

def Division():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if b == 0:
        print("Ошибка: деление на ноль невозможно.")
    else:
        print(f"Частное: {a} / {b} = {a / b}")

def PrintMenu():
    print("\n--=- Главное меню --=-")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")

def main():
    while True:
        PrintMenu()
        number = input("Выберите пункт меню: ")

        if number == '1':
            Addition()
        elif number == '2':
            Subtraction()
        elif number == '3':
            Multiplication()
        elif number == '3':
            Division()
        elif number == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод, попробуйте еще раз")


if __name__ == "__main__":
    main()
