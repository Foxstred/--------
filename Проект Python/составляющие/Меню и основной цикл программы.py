#меню
MENU_TEXT="""1. Решение линейных квадратных уравнений
2.  Решение квадратных уравнений
3. Построение арифмитичсекой прогрессии 
4. Арифмитические операции с дробями"""
print("Приветствуем! Это решатор, который поможет вам с некоторыми математическими задачами")
print("Мы можем помочь вам со следующими пунктами:")
print(MENU_TEXT)
print("Введите номер интересующего вас пункта")
user_choice=input()
#основной цикл программы
while user_choice!="0":
    if user_choice=="1":
        print("Пункт в разработке")
    elif user_choice=="2":
        print("Пункт в разработке")
    elif user_choice=="3":
        print("Пункт в разработке")
    elif user_choice=="4":
        print("Пункт в разработке")
    else:
        print("Это явно не число или номер, которого нет в меню!")
    
    print("_"*87)
    
    print(MENU_TEXT)
    print("Введите номер интересующего вас пункта или 0, если хотите завершить работу с программой")
    user_choice=input()

print("Благодарим вас за использование нашего сервиса! До встречи!")

    