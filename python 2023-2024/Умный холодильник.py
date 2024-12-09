product, num = input().split()
num = int(num)


while not(product == "закрыть 0"):
    if num>0:
        print(f"{product}: {num}")
        if product!="хлеб":
            print("хлеб: 0")
            if product!="шоколадки":
                print("шоколадки: 0")
                if product!="молоко":
                    print("молоко: 0")              
    if product!="хлеб":
            print("нужно купить хлеб")
            if product!="шоколадки":
                print("нужно купить шоколадки")
                if product!="молоко":
                    print("нужно купить молоко")   
  
    print(" __________")    
    
    
    
    
    
    product, num = input().split()
    num = int(num)
    
