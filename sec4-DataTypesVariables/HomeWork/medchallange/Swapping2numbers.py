'''
Write a program that reads 2 integers num1 and num2
-E.g. say we read num1 = 7 and num2 = 25

'''

num1,num2=map(int,input("Enter two number: ").split())
sawp=num1
num1=num2
num2=sawp

print(num1 , num2)