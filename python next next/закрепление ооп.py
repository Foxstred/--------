def sumdigits(number: int)->int:
    lst=[int(i) for i in str(number)]
      
    return sum(lst) 

def main():
    number: int=int(input())
    print(sumdigits(number))

if __name__=='__main__':
    main()