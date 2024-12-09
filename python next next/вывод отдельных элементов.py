
def num_even(num: int, nums: list)->int:
   
    lst=[i for i in nums if i%2==0]

    print(*lst)


def main()->None:
    num: int=int(input())
    nums: list[int] = list(map(int, input().split()))
    num_even(num, nums)

if __name__ =="__main__":
    main()