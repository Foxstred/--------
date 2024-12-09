class Human:
    name=str()
    hp=int()
    power=int()
    hunger=int()
    happiness=int()
    def print_info(self):
        print(f"Имя: {self.name} Здоровье: {self.hp} Сила: {self.power} Голод: {self.hunger} Счастье: {self.happiness}")
    def eat(self):
        self.power+=2 
        self.hunger*=0            
        self.happiness+=1
    def sleep(self):
        self.hp+=2
        self.power+=3
        self.hunger+=4
        self.happiness+=2
hero=Human()
hero.name = 'Олег'
hero.hp = 6
hero.power = 4
hero.hunger = 10
hero.happiness = 2


local=Human()
local.name=input()  # local
local.hp=int(input())
local.power=int(input())
local.hunger=int(input())
local.happiness=int(input())
local.eat()
print(f'Сила местного = {local.power}')
tool=input()
hero.tools=tool
print(f'Найдено орудие {hero.tools} ! Ура!')
local.print_info()
hero.print_info()