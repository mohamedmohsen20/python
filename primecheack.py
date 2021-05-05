num=int(input("plz enter num"))
flag=False

if num > 1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break

if flag:
    print(num,"not prime")
else :
    print(num ,"is prime")
