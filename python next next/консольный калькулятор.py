class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            return "Ошибка: Деление на ноль!"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def percentage(self, a, b):
        result = (a * b) / 100
        self.history.append(f"{b}% от {a} = {result}")
        return result

    def show_history(self):
        if not self.history:
            return "История пустая."
        return "\n".join(self.history)

    def display_menu(self):
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Нахождение процента")
        print("6. Показать историю вычислений")
        print("7. Выход")

def main():
    calc = Calculator()

    while True:
        calc.display_menu()
        choice = input("Укажите пункт меню: ")

        if choice == '7':
            print("Выход из программы.")
            break

        if choice in ['1', '2', '3', '4', '5']:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))

            if choice == '1':
                print(f"Результат: {calc.add(a, b)}")
            elif choice == '2':
                print(f"Результат: {calc.subtract(a, b)}")
            elif choice == '3':
                print(f"Результат: {calc.multiply(a, b)}")
            elif choice == '4':
                print(f"Результат: {calc.divide(a, b)}")
            elif choice == '5':
                print(f"Результат: {calc.percentage(a, b)}")

        elif choice == '6':
            print(calc.show_history())
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()