def max_by_abs(my_list):
    answer=0
    new_lst=[abs(i) for i in my_list]
    maxi=max(new_lst)
    for i in range(len(new_lst)):
        if new_lst[i]==maxi:
            answer=my_list[i]
    return answer
my_list=list(map(int,input().split()))
ans=max_by_abs(my_list)
print(ans)  
