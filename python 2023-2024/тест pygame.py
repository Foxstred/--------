class Human:
    name=str()
    hp=int()
    power=int()
    hunger=int()
    happiness=int()
    tools=[]
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
    def collect_tool(self, x):
        print(f'Найдено орудие {x} ! Ура!')              
        tools.append(x)  
hero = Human()
hero.name = ''
hero.hp = 6
hero.power = 4
hero.hunger = 10
hero.happiness = 2
print(hero.name, hero.hp, hero.power, hero.hunger, hero.happiness)
hero.eat()
hero.sleep()
hero.print_info()
hero.collect_tool("")
hero.collect_tool("камень")
hero.collect_tool("палка")
print(*hero.tools)