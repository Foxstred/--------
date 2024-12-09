def the_end(num: int, number: int)->int:
    lst=str(number)
    if len(lst)>3 and num!=0:
        lst=lst[:len(lst)-3]+str(num)+lst[len(lst)-3:]
        print(lst)
    elif num==0 and len(lst)<=3:
        print(lst)
    elif num!=0:
        lst=lst[:len(lst)-3]+str(num)+lst[len(lst)-3:]
        print(lst)
    elif num==0 and len(lst)>3:
        lst=lst[:len(lst)-3]+str(num)+lst[len(lst)-3:]
        print(lst)


def main()->None:
    num: int=int(input())
    number: int=int(input())
    the_end(num, number)

if __name__ == '__main__':
    main()