'''

Given 8 space-separated integers, find the sum of those in even places and
the sum of those in odd places


Input: 11 2 7 9 12 -8 3 -1
Output: 2 33
11 + 7 + 12 + 3 = 33 for the odd places
'''

odd1,even1,odd2,even2,odd3,even3,odd4,even4=map(int,input("enter 8 integer numbers !!").split())
#cal sum odd inputs
sum_odd=odd1+odd2+odd3+odd4

#cal sum even inputs
sum_even=even1+even2+even3+even4

#print final res

print(sum_odd,"",sum_even)

