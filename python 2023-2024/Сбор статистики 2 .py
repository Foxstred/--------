name = input()
something = input()
 
if something == 'лайк' or something == 'комментарий':
    num = int(input())
while something != 'выход':
    if something == 'лайк':
        print("Пользователь", name, "поставил вам", num, "лайков")
    elif something == 'комментарий':
        print("Пользователь", name, "оставил вам", num, "комментариев")
    elif something == 'подписка':
        print("Пользователь", name, "подписался на вас")
    name = input()
    something = input()
         
    if something == 'лайк' or something == 'комментарий':
        num = int(input())

            
       
    