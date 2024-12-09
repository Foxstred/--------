#Импорт
from math import sqrt 
#доп.переменные 
MENU_TEXT="""1. Решение линейных уравнений
2. Решение квадратных уравнений
3. Построение арифметической прогрессии
4. Арифметические операции с дробями"""
#первый ввод меню
print("Приветствуем! Это решатор, который поможет вам с некоторыми математическими задачами")
print("Мы можем помочь вам со следующими пунктами:")
print(MENU_TEXT)
print("Введите номер интересующего вас пункта")
user_choice=input()
#основные циклы программы 
while user_choice!="0":
    if user_choice=="1":
        print("Общий вид линейного уравнения: ax + b = 0")
        print("Введите значения коэффициентов a и b через пробел")
        
        a,b =map(float,input().split()) #нужна проверка 
        
        x= -b/a
        print(f"Ответ: x = {x}")
    elif user_choice=="2":
        print("Общий вид квадратного уравнения: ax^2 + bx + c = 0")
        print("Введите значения коэффициентов a, b и c через пробел")
        
        a, b, c =map(float, input().split())#нужна защита от пользователя 
        d=b**2 - 4*a*c
        if d<0:
            print("Данное уравнение не имеет решений")
        elif d==0:
            x=-b/(2*a)
            print(f"Ответ: x = {x}")
        else:
            x1=(-b+sqrt(d))/(2*a)
            x2=(-b-sqrt(d))/(2*a)
            print(f"Ответ: x1 = {x1}, x2 = {x2}")
    elif user_choice=="3":
        print("Введите значение первого элемента прогрессии")
        
        elem=int(input())#проверка 
        
        print("Введите значение разности между соседними элементами")
       
        step=int(input())
        print("Выберите один из трех пунктов, введя соответствущий номер")
        print("1. Вывести все элементы прогрессии")
        print("2. Вывести номер элемента прогрессии, равного определенному значению")
        print("3. Вывести значение элемента прогрессии под определенным номером")
        # Нужна защита как в меню
        user_choice=int(input())
        if user_choice==1:
            print("Введите количество элементов в прогрессии")
           
            length=int(input())
            print("Получившая арифметическая прогрессия:")
            print(elem, end=' ')
            for _ in range(length-1):
                elem+=step
                print(elem, end=' ')
            print()
        elif user_choice ==2:
            print("Введите значение элемента прогрессии:")
            elem_need=int(input())
            
            elem_counter=1
            while elem < elem_need:
                elem+=step
                elem_counter += 1
            if elem==elem_need:
                print(
                    f"Элемент со значением {elem_need} находится под номером {elem_counter}"
                )
            else:
                    print("Искомого элемента нет в прогрессии(")
        elif user_choice==3:
            print("Введите номер элемента прогрессии:")
            
            number_need = int(input())    
            for _ in range(number_need-1):
                elem+=step
            
            print(f"Элемент под номером {number_need} имеет значение {elem}")
    elif user_choice=="4":
        print("Введите числитель и знаменатель первой дроби через пробел")

        x1, y1 = map(int, input().split())
        
        print("Введите числитель и знаменатель второй дроби через пробел")
        
        x2, y2 = map(int, input().split())
        
        print("Введите номер операции, которую вы хотите применить к данным дробям")
        
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        user_choice=int(input())
        
        if user_choice==1:
            answer_x=x1*y2+x2*y1
            answer_y=y1*y2
            print(f"{x1}/{y1} + {x2}/{y2} = ", end='')
        elif user_choice==2:
            answer_x = x1 * y2 - x2 * y1
            answer_y = y1 * y2
            print(f"{x1}/{y1} - {x2}/{y2} = ", end='')
        elif user_choice == 3:
            answer_x = x1 * x2
            answer_y = y1 * y2
            print(f"{x1}/{y1} * {x2}/{y2} = ", end='')
        elif user_choice == 4:
            answer_x = x1 * y2
            answer_y = y1 * x2
            print(f"{x1}/{y1} / {x2}/{y2} = ", end='')    
            
        NOD = abs(answer_x)
        if NOD > abs(answer_y):
            NOD = abs(answer_y)
        while not (answer_x % NOD == 0 and answer_y % NOD == 0):
            NOD -= 1
            
        answer_x //= NOD
        answer_y //= NOD
        print(f"{answer_x}/{answer_y}")
    else:
        print("Это явно не число или номер, которого нет в меню!")
    
    print("_"*87)
    
    print(MENU_TEXT)
    print("Введите номер интересующего вас пункта или 0, если хотите завершить работу с программой")
    user_choice=input()
#ин-фа о завершение работы программы 
print("Благодарим вас за использование нашего сервиса! До встречи!")