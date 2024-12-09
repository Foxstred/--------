from math import floor

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = map(int, input().split())

money=0
tovar=0

for i in n1, n2, n3, n4, n4, n6, n7, n8, n9, n10:
    money=money+i//10
    tovar=tovar+i%10

all_money=floor(money/10)
print(all_money, tovar)