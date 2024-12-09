import math

class Point:
    def __init__(self, x: int, y: int)-> None:
        self.__x: int=x
        self.__y: int=y 
        
    def math_distance(self, start_x: int=0, start_y: int=0)-> float:
        answer: float=math.sqrt((start_x-self.__x)**2+(start_y-self.__y)**2)
        return answer
    def print_coords(self)->None:
        print(f"{self.__x}{self.__y}")
    
def read_points(count: int)-> tuple[Point, ...]:
    points: list[Point]=[]
    for _ in range(count):
        
        x: int 
        y: int 
        x, y=map(int, input().split())
        points.append(Point(x,y)) 
        
    return tuple(points)

def find_max_distance(points: tuple[Point, ...])-> tuple[Point, ...]:
    max_distance: float=points[0].math_distance()
    max_distance_points: list[Point]=[points[0]]
    
    for point in points[1:]:
        distance: float=point.math_distance()
        if distance>max_distance:
            max_distance=distance
            max_distance_points=[point]
        elif distance==max_distance:
            max_distance_points.append(point)

    return tuple(max_distance_points)

def print_points_info(points: tuple[Point, ...])->None:
    for point in points:
        point.print_coords()

def main()-> None:
    point_count=input()
    point_count=int(point_count)
    points: tuple[Point, ...]=read_points(point_count)
    answer: tuple[Point, ...]=find_max_distance(points)
    print_points_info(answer)

if __name__=="__main__":
    main()

        