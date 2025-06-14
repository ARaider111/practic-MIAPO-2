def PrintMenu():
    print("\n--- Главное меню ---")
    print("0. Выход")

def main():
    while True:
        PrintMenu()
        num = input("Выберите пункт меню: ")

        if num == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод, попробуйте еще раз")


if __name__ == "__main__":
    main()
