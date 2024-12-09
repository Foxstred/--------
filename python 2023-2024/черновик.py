class CommonFraction:
    def __init__(self,text):
        text=text.split('/')
        self.__x=int(text[0])
        self.__y=int(text[1])

# Типы данных
    def __str__(self):
        return f"{self.__x}/{self.__y}"
    def __int__(self):
        return self.__x//self.__y    
    def __float__(self):
        return self.__x/self.__y
# Добавление копии    
    def __add__(self, other):
        new_x=self.__x*other.get_y()+other.get_x()*self.__y
        new_y=self.__y*other.get_y()
        return CommonFraction(f"{new_x}/{new_y}")
# Создание копии
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
# Модуль       
    def __abs__(self):
        if self.__x<0 and self.__y>0:
            return f"{self.__x*(-1)}/{self.__y}"
        elif self.__y<0 and self.__x>-1:
            return f"{self.__x}/{self.__y*(-1)}"
        elif self.__y<0 and self.__x<0:
            return f"{self.__x*(-1)}/{self.__y*(-1)}"
        else:
            return f"{self.__x}/{self.__y}"
# Возведение в степень    
    def  __pow__(self, power):
        new_x=self.__x**power 
        new_y=self.__y**power 
        return f'{new_x}/{new_y}'
# Длина числа     
    def __len__(self):
        if self.__x<0 and self.__y>0:
            self.__x*=-1
        elif self.__y<0 and self.__x>0:
            self.__y*=-1
        elif self.__y<0 and self.__x<0:
            self.__x*=-1
            self.__y*=-1
        str_x=str(self.__x)
        str_y=str(self.__y)
        suma=len(str_x)+len(str_y)
        return suma
    
    
    #def __shorts__(self):
        
        
def main():
    a = CommonFraction(input())
    b = CommonFraction(input())
    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)


if __name__ == '__main__':
    main()