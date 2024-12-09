def sumdigits(number: int)->int:   
    lst=[number//10, number%10]  
    print(*lst)
    

def main():
    number: int=int(input())
    sumdigits(number)

if __name__=='__main__':
    main()