def player_greeting():
    print("""__________________________________________________________________________________________
Добро пожаловать в игру «Морской бой!»
Данная игра позволяет сыграть против друга в увлекательную водную стратегию.
Игроки делают свои ходы по очереди, поэтому не стоит подсматривать в экран во время хода противника.
Приятной игры! 😍
------------------------------------------------------------------------------------------""")

player_greeting()


def show_fill_table_instruction():
    print("""__________________________________________________________________________________________  
Тебе нужно расставить свои корабли, игрок
Поочередно тебе будет предложено выбрать местоположение каждого корабля
Для каждого из них:
	1. Выбираешь координату первого квадратика
	2. Указываешь, нужно ли расположить корабль вертикально или горизонтально (только не для однопалубных)

Учитывай, что в этой игре нет проверки того, что корабли находятся рядом друг с другом (тут на честность)
	 и проверки того, что корабль вышел за границы поля (тут ты просто словишь ошибку)

Расставляй корабли с умом!
------------------------------------------------------------------------------------------
    """)

show_fill_table_instruction()


def show_table(table):
    print("""   1 2 3 4 5 6 7 8 
    _______________""")
    for i in range(len(table)):
        print(f"{i+1} |",end='')
        print(*table[i],end='|\n')
    print("   ---------------")

def put_ship(table, x, y, ship_size):
    x,y=x-1, y-1
    
    if ship_size!=1:
        print("Корабль будет расположен вертикально (1) или горизонтально(2)?")
        sync=int(input())
        if sync==1:            
            for i in range(y,y+ship_size):
                table[i][x]="#"
        else:
            for i in range(x, x+ship_size):
                table[y][i]="#"
    else:
        table[y][x]='#'

def fill_table(table):
    show_fill_table_instruction()
    
    show_table(table)
    
    print("Введи x и y первой ячейки четырёхпалубного корабля:")
    x,y=map(int,input().split())
    put_ship(table, x, y, 4)
    show_table(table)
    
    for _ in range(2):
        print("Введи x и y первой ячейки трёхпалубного корабля:")
        x,y=map(int,input().split())
        put_ship(table, x, y, 3)
        show_table(table)
    
    for _ in range(3):
        print("Введи x и y первой ячейки двухпалубного корабля:")
        x,y=map(int,input().split())
        put_ship(table, x, y, 2)
        show_table(table)
    
    for _ in range(4):
        print("Введи x и y первой ячейки однопалубного корабля:")
        x,y=map(int,input().split())
        put_ship(table, x, y, 1)
        show_table(table)

def get_table():
    table=[]
    for _ in range(8):
        table.append(['~' for _ in range(8)])
    fill_table(table)
    return table
    

s = get_table()
print()
for line in s:
    print(*line)