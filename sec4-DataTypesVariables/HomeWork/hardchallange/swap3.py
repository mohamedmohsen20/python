'''
Write a program that reads 2 integers a ,b,c
a=b
b=c
c=a

'''

num1,num2,num3=map(int,input("Enter two number: ").split())
sawp=num1
num1=num2
num2=num3
num3=sawp

print(num1 , num2 ,num3)