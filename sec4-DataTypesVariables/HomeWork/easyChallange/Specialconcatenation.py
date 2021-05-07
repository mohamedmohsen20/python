'''
Write a program that read 3 strings.
-For simplicity let’s say input is 3 letters A, B and C
The output is A’B”C repeated 10 times
-A’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”C


'''

a,b,c=input("Enter 3 strings: ").split()

s=a+"'"+b+"\""+c
print(s*10)