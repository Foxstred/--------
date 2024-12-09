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


class Taxi(Car):
    def __init__(self, cost: int)->None:
        super().__init__()
        self.cost = cost   # Цена за одну пройденную единицу расстояния
        self.distance = 0  # Пройденное растояние

    def get_total_cost(self)->int:
        """
        Подсчитать цену поездки
        """
        return self.cost*self.distance

    def reset(self)->None:
        """
        Сбросить пройденное расстояние
        """
        self.distance=0

    def move(self, direction:int)->int:
        """
        Модифицированный метод движения для подсчета пройденного расстояния
        """
        super().move(direction)
        self.distance+=abs(direction)

def main() -> None:
    K: int
    cost: int
    K, cost=map(int,input().split())
    taxi = Taxi(cost=cost)  # Исправлено создание объекта Taxi
    
    for _ in range(K):
        command: list = input().split()
        if command[0] == 'MOVE':
            d = int(command[1])
            taxi.move(d)
        elif command[0] == "POSITION":
            print(taxi.get_position())
        elif command[0] == "COST":
            print(taxi.get_total_cost())
    

if __name__ == "__main__":
    main()
