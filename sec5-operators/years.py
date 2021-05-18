'''
                    years
    Assume a year is 12 months, but each month is 30 days
    -That is a year has 12 * 30 = 360 days
Read an integer: whole number of days of someone age. Print 3 numbers
    -Total years total months remaining days



    5000   13 10 20

'''


nDays=int(input("enter no of days : "))
#cal years
years=nDays//360
#cal days without years
days=nDays%360
#cal monthes
monthes=days//30
#nDays=((years*360)+(monthes*30))+days
days=nDays-((years*360)+(monthes*30))
 


print(years," ", monthes," ",days)
