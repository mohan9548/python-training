for a in range(2,100+1):
    if all(a%i!=0 for i in range(2,int(a**0.5)+1)):
        print(a)