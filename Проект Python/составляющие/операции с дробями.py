#Дроби 


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
    answer-x=x1*y2+x2*y1
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
    
    