'''

            Implement the following 2 functions:
        -is_prime(num);

        -nth_prime(n);
-Return the n-th prime number. It should use is_prime function
-E.g nth_prime(6) = 13
Recall primes are: 2, 3, 5, 7, 11, 13, 17, 19



'''

def is_prime(num):
    if num==2 :
       return True
    if num==0 or num==1:
        return False 
    for n in range(2,num):
        if num%n==0:
            status= False
            break
        else:
            status= True 
    return status

def nth_prime(n):
    ll=[]
    start=2
    while  n != len(ll):
        if is_prime(start)==True:
            ll.append(start)
            start+=1
        else:
            start+=1
    return ll    

        



res=nth_prime(10)
for i in range(1,10):
    print(i,res[i])

