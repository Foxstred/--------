def is_power(N: int,numbers: list, A: int)-> int:
    count=0
    
    numbers_set=set(numbers)
    for i in numbers:
        if i==A:
            count+=1
    numbers_set=set(numbers)
    power=A**0
    while power<=max(numbers):
        if power in numbers_set:
            count+=1
        power*=A
        

    print(count)

def main()->None:
    N: int=int(input())
    
    numbers: list=list(map(int,input().split()))
    
    A: int=int(input())
    is_power(N,numbers,A)
    


if __name__ == '__main__':
    main()


    
