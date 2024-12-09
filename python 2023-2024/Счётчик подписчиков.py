c_sub_orig = int(input())  # Изначальное кол-во подписчиков
c_sub = c_sub_orig  # Создание новой переменной, которую будем менять

command = input()
while command != "конец":
    symbol, num = command.split()  # Разделение команды на две переменные по пробелу
    num = int(num)  # Приведение строки к числу
    if symbol == '+':
        c_sub = c_sub + num
    else:
        c_sub = c_sub - num
    command = input()

if c_sub > c_sub_orig:
    print("YES")
else:
    print("NO")

