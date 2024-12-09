class katalog:
    
    def __init__(self, model, cpu_model, hdd_size):
        self.model=model
        self.cpu_model=cpu_model
        self.hdd_size=hdd_size
        self.correct_hdd_size()
    def correct_hdd_size(self):
        self.hdd_size*=1
    def __del__(self):
        print(f"{self.model} продали")    
    def print_info(self):
        print(f'{self.model}\n\tПроцессор: {self.cpu_model}\n\tПЗУ: {self.hdd_size}\n')

# Таблица
print("""1. Добавить ноутбук
2. Показать ноутбуки
3. Продать ноутбук
4. Изменить объем памяти ноутбука
5. Выйти из программы""")
# выбор пользователя 
user_choice=int(input())
# цикл выбора 
#laptop=katalog()
lst=[]
while user_choice<6:
    #if user_choice>4 or user_choice<1:
        #print("Неправильный ввод")
    if user_choice==1:
        model, cpu_model, hdd_size=input().split(',')
        hdd_size=int(hdd_size)
        laptop=katalog(model, cpu_model, hdd_size)  
        lst.append(laptop)
    elif user_choice==2:
        for i in range(len(lst)):
            lst[i].print_info()
    elif user_choice==4:
        print("Введите номер ноутбука, память которого нужно поменять")
        num_of_change=int(input())  
        print("Введите новое количество памяти")
        new_memory=int(input())   
        lst[num_of_change-1].hdd_size=new_memory
        laptop.print_info()
    elif user_choice==3:
        print("Введите номер ноутбука, который нужно продать")
        num_of_sell=int(input())
        del lst[num_of_sell-1]
    elif user_choice==5:
        del laptop
    user_choice=int(input())
    