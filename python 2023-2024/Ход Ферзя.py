#Путь ферзя 
#x1, y1 (координаты ферзя); x2, y2 (координаты клетку которую должен побить)
# 1-если бьет клетку, 2-если не бьет клетку 
x1,y1,x2,y2 =map(int,input().split())
if x1==x2 and y1==y2:
    print(0)
elif x1==x2 or y1==y2:
    print(1)
elif x1-y1==x2-y2:
    print(1)
elif x1+y1 == x2+y2:
    print(1)
else:
    print(0)
    