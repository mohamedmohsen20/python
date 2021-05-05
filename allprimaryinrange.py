#this app to print no of primary num in an interval

a=int(input("enter first of interval : "))

b=int(input("enter first of interval : "))

for num in range(a,b+1):
    if num > 0:
        for i in range (2,num):
            if(num%i)==0:
                break
        else:
            print(num)
                
