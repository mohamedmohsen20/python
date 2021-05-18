'''
                    Our remainder
            Write a program that reads 2 positive integers and print such reminder without
            using the modulus operator %

            Input: 27 12
            Output: 3
'''

#reads 2 positive integers

num1 , num2 = map(int,input("enter two postive integers").split())

#operation 27%12 ==  3
#  27 = (12*2 + 3)
#27//12 = 2
k=num1 // num2
res=num1-(num2*k)

print(res)


