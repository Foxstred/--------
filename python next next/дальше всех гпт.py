import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

def main():
    n: int=int(input())
    points = []

    for _ in range(n):
        x: int
        y: int
        x, y = map(int, input().split())
        points.append(Point(x, y))

 
    max_distance = max(point.distance() for point in points)

    for point in points:
        if math.isclose(point.distance(), max_distance):
            print(point.x, point.y)

if __name__ == "__main__":
    main()