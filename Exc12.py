'''
Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει μια ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ και εμφανίζει πόσες μέρες/ώρες/δευτερόλεπτα
απέχει αυτή από την τρέχουσα ημερομηνία του υπολογιστή, καθώς και πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας.

'''
import time

#Getting the current date
t = time.localtime()

#Calculating the number of days since 00/00/00
now_int = 365*t.tm_year + 30*t.tm_mon + t.tm_mday

#User input
print("Give me the date you want to calculate the chronological distance from (DD/MM/YYYY):")
date = input()
#Calculating the number of days since 00/00/00 again
date_split = date.split("/")
date_int = 365*int(date_split[2])+30*int(date_split[1])+int(date_split[0])

#Finding the chronological distance between now and the date given
d = abs(now_int - date_int)

#Turning it into days,months,years
dif = [0, 0, 0]
dif[2] = int(d/365)
dif[1] = int((d%365)/30)
dif[0] = int((d%365)%30)

#Preparing data for printing
printStatus = "The difference is "
if dif[0] > 1:
    printStatus += str(dif[0])+" days "
elif dif[0] == 1:
    printStatus += str(dif[0])+" day "

if dif[1] > 1:
    printStatus += str(dif[1])+" months "
elif dif[1] == 1:
    printStatus += str(dif[1])+" month "

if dif[2] > 1:
    printStatus += str(dif[2])+" years "
elif dif[2] == 1:
    printStatus += str(dif[2])+" year "
print(printStatus)

#Defigning leap years
leapYear = False
y = int(date_split[2])
if int(y%4)==0 and int(y%100)!=0:
    leapYear = True
if int(y%400)==0:
    leapYear = True

#Finding how many days the month has
m = int(date_split[1])
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    days = 31
elif m==2:
    if leapYear:
        days = 29
    else:
        days = 28
else:
    days = 30

print("That month has "+str(days)+" days")
