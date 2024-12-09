import math

def distanse(point1: int, point2: int, point3: int)-> int:
    x1: int
    y1: int
    x1, y1=point1
    x2: int
    y2: int
    x2, y2=point2
    x3: int
    y3: int
    x3, y3=point3
    dist1=math.sqrt((x2-x1)**2+(y2-y1)**2)
    dist2=math.sqrt((x3-x2)**2+(y3-y2)**2)
    dist3=math.sqrt((x3-x1)**2+(y3-y1)**2)
    print(dist1+dist2+dist3)

def main()->None:
    point1: int=map(int,input().split())
    point2: int=map(int,input().split())
    point3: int=map(int,input().split())
    distanse(point1, point2, point3)
if __name__ == '__main__':
    main()


        
