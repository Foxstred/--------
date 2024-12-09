class Bus:
    def __init__(self, P, C):
        self.position = P  # Начальная позиция троллейбуса
        self.capacity = C  # Вместимость троллейбуса
        self.passengers = {}  # Словарь для хранения пассажиров по остановкам

    def move(self, d):
        self.position += d

    def get_position(self):
        return self.position

    def board_passenger(self, k):
        if len(self.passengers) < self.capacity:
            self.passengers[k] = self.passengers.get(k, 0) + 1
            return "SUCCESS"
        else:
            return ":("

    def release_passengers(self, k):
        if k in self.passengers:
            del self.passengers[k]

    def count_passengers(self):
        return sum(self.passengers.values())


class Trolleybus(Bus):
    def __init__(self, P, C, L, R):
        super().__init__(P, C)
        self.L = L  # Левая граница перемещения
        self.R = R  # Правая граница перемещения

    def move(self, d):
        new_position = self.position + d
        if self.L <= new_position <= self.R:
            self.position = new_position
        else:
            print("Out of bounds")


def main():
    K, P, C, L, R = map(int, input().split())
    trolleybus = Trolleybus(P, C, L, R)

    for _ in range(K):
        command = input().strip().split()
        
        if command[0] == "MOVE":
            if len(command) > 1:
                d = int(command[1])
                trolleybus.move(d)
                
        elif command[0] == "POSITION":
            print(trolleybus.get_position())
            
        elif command[0] == "PASSENGER":
            if len(command) > 1:
                k = int(command[1])
                print(trolleybus.board_passenger(k))
                
        elif command[0] == "RELEASE":
            if len(command) > 1:
                k = int(command[1])
                trolleybus.release_passengers(k)
                
        elif command[0] == "PASSENGERS":
            print(trolleybus.count_passengers())


if __name__ == "__main__":
    main()