
def Addition():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a} + {b} = {a + b}")

def Subtraction():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a} - {b} = {a - b}")

def PrintMenu():
    print("\n--- Главное меню ---")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")

def main():
    while True:
        PrintMenu()
        num = input("Выберите пункт меню: ")

        if num == '1':
            Addition()
        elif num == '2':
            Subtraction()
        elif num == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод, попробуйте еще раз")


if __name__ == "__main__":
    main()
