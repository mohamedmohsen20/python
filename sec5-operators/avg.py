'''
                    Averages
                Write a program that reads 5 numbers and print the following:
A) Their average
B) The sum of the first 3 numbers divided by the sum of the last 2 numbers
C) The average of the first 3 numbers divided by the average of the last 2 numbers.
What is the math relation between B and C?

ex:
Input 1 2 3 4 5
3
0.666666667
0.444444444

'''
#reads 5 numbers

num1,num2,num3,num4,num5=map(float,input("enter 5 numbers : ").split())

#Their average
avg=(num1+num2+num3+num4+num5)/5

print("avg = ",avg )


#The sum of the first 3 numbers divided by the sum of the last 2 numbers

sumofThree=num1+num2+num3
sumofLast=num4+num5
res=sumofThree/sumofLast
print(res)


#The average of the first 3 numbers divided by the average of the last 2 numbers
avgofThree=sumofThree/3
avgofLast=sumofLast/2
res=avgofThree/avgofLast
print(res)

#relation between B and C? c=2B/3