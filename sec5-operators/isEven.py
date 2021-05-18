'''
        Is even?
        The following code, reads an integer and computes a boolean if the number is
          even in 3 different ways. The number can be +ve or -ve.
    Fill in the is_even to solve the problem in 3 ways as following
    - Using only %2
    - Using only %10
    - Using only /2
'''


#read int
num=int(input("enter num : "))

#- Using only %2

iseven1=(num%2==0)


#- Using only /2       

iseven2=((num/2)-int(num/2) ==0)

#- Using only %10

iseven3=num%10
iseven3=(iseven3 == 0 or iseven3 == 2 or iseven3 == 4 or iseven3 == 6 or iseven3 == 8)

print(iseven1," ",iseven2," ",iseven3)



#- Using  num/2 - num//2 =0

iseven4=((num/2)-(num//2) ==0)
print(iseven4)