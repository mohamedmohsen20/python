'''
reads 2 students information about math exam
For each student read: his name, id and grade
Print the students
Print the grades average

'''

std1_name = input("Enter the first student's name: ")
std1_age = int(input("Enter the first student's ID: "))
std1_grade = float(input("Enter the first student's grade: "))

std2_name=input("Enter the second student's name: ")
std2_age=int(input("Enter the second student's ID: "))
std2_grade=float(input("Enter the second student's grade: "))

#print all info
print('Informat for students and their "Math" grades')

print(std1_name,"(",std1_age,") got grade :",std1_grade )

print(std2_name,"(",std2_age,") got grade :",std2_grade )

#Print the grades average

avg=(std1_grade+std2_grade)/2.0
print("average = ",avg)
