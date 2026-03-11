#Q1
n = int(input())

if n % 2 != 0:
    print("Weird")

elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")

elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")

elif n % 2 == 0 and n > 20:
    print("Not Weird")

#2nd approch:

import sys
n=int(input())
if n%2==1 or n in range(5,21):
    print("Weird")
else:
    print("Not Weird")
    
# 3rd approach:

n=int(input())
if n%2!=0:
    print("Weird")
    exit()
if 2<=n<=5:
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")  


#Q2
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
#Q3
a = int(input())
b = int(input())

print(a // b)
print(a / b)

#Q4
n = int(input())

for i in range(n):
    print(i * i)

#Q5
#1st approch
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap
#leap year  2nd approch:
def is_leap(year):
    return (year%4==0 and year%100!=0) or (year %400==0)


year = int(input())
print(is_leap(year))
#Q6
n = int(input())

for i in range(1, n + 1):
    print(i, end="")

