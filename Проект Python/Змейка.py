from random import randint, seed
seed(10)

a, b=map(int,input("Введите размер поля: ").split())
lst=[['.' for _ in range(a)] for _ in range(a) ]

print()
#Создание змейки
snake = [[a//2,b//2]]
#Создание еды
fs=[
    [y,x]
    for y in range(a)
    for x in range(b)
    if [y,x] not in snake
]
apple_y, apple_x = fs[randint(0,len(fs)-1)]
#y, x=randint(0,a-1), randint(0,b-1)
lst[apple_y][apple_x]='+'

print()
    
pole=[i.copy() for i in lst]     
for sp in snake:
    pole[sp[0]][sp[1]]='*'
for i in pole:
    print(*i)

print()
#Движение
print('Куда двигаемся?')
menu=(
"""8. вверх
4. влево
6. вправо
4. влево
"""   
)
print(menu)
d=int(input()) 
while d!=0:
    start=snake[0][0]
    end=snake[0][1]    
    if d==8:
        start-=1                  
    elif d==2:
        start+=1                
    elif d==4:
        end-=1    
    elif d==6:
        end+=1            
    snake.insert(0, [start,end])
    
    if pole[start][end]!='+':
        snake.pop()
    else:
        lst[start][end]='.'
        y, x=randint(0,a-1), randint(0,b-1)
        lst[y][x]='+'            
    pole=[i.copy() for i in lst]        
    for sp in snake:
        pole[sp[0]][sp[1]]='*'
    for i in pole:
        print(*i)
    print(menu)
    d=int(input())

print()


