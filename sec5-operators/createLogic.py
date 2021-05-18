'''

-Write a program that reads 3 integers about the class room
    Number of boys (nb), number of girls (ng), number of teachers (nt)
-Prepare and print a boolean variable for these cases:
    nb greater than 25
    ng less than or equal to 30
    nb > 20 and nt > 2 or ng > 30 and nt > 4
    Either nb < 60 or ng < 70
    Neither nb >= 60 nor ng >= 70

'''

nb , ng , nt = map(int,input("enter nb ng nt").split())

#nb greater than 25
print(nb > 25)

# ng less than or equal to 30
print(ng <= 30)

#nb > 20 and nt > 2 or ng > 30 and nt > 4

print(nb > 20 and nt > 2 or ng >30 and nt>4)

#Either nb < 60 or ng < 70
print(nb < 60 or ng <70)

#Neither nb >= 60 nor ng >= 70
print(not nb >=60 and not ng >=70)


