num1 , sign , num2 =input("enter the nums ").split()
num1 , num2 =float(num1), float(num2)

if sign == "+":
    print(num1+num2)

elif sign == "-":
    print(num1-num2)

elif sign == "*":
    print(num1*num2)

elif sign == "/" and num2 !=0:
    print(num1-num2)

elif sign == "/" and num2 ==0:
    print("not valid")