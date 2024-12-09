class Car:
    def __init__(self)->None:
        """
        По умолчанию, позиция машины равна 0
        """
        self.pos = 0

    def move(self, direction: int)->None:
        """
        Сдвинуться по числовой прямой на расстояние direction
        Если direction < 0, то влево
        Если direction > 0, то вправо
        """
        self.pos += direction

    def get_position(self)->int:
        """
        Узнать текущую позицию автомобиля
        """
        return self.pos

def main()->None:
    K:int=int(input())
    car:Car=Car()

    for _ in range(K):
        command:list=input().split()
        if command[0]=='MOVE':
            d=command[1]
            d:int = int(d)
            car.move(d)
        elif command[0] == "POSITION":
            print(car.get_position())

if __name__ == "__main__":
    main()