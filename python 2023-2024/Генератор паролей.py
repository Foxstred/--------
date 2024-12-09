import random 
str1='123456789'
str2='qwerty'
str3=str2.upper()
str4='---'
str5=str1+str2+str3+str4
lst=list(str5)
random.shuffle(lst)

psw=''.join([random.choice(lst) for i in range(12)])
print(psw)