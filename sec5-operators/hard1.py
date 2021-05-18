'''
                Write a program that reads an integer and print 100 if number is even or 7 if
                number is odd
E.g. for input 8 ⇒ 100
E.g. for input 133 ⇒ 7

'''

num=int(input("enter the number"))
even=100
odd = 7
x=((num%2==0 and even) or (num%2==1 and odd))
print(x)