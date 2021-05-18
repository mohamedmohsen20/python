'''

                Last 3 digits sum
    Write a program that reads an integer and prints the sum of its last 3 digits
    Inputs ⇒ Outputs examples

15⇒ 6

125⇒ 8
1000⇒ 0
1001⇒ 1
1234⇒ 9
99999⇒ 27

'''


num=int(input("enter the num"))
sum=0
# remember
# number % 10   => gets the last digit
# number // 10  => removes the last digit

# logic: get digit, remove it. Apply 3 times to get the last 3 digits
rem1=num%10
sum+=rem
num=num//10

rem2=num%10
sum+=rem
num=num//10

rem3=num%10
sum+=rem
num=num//10


print(sum)