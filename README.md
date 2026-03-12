# Python101
#user input
a=int(input("enter any number:"))
b=int(input("enter any number:"))
c=a+b
print("addition= ",c)



# find your current age 
a=int(input("enter current year:"))
b=int(input("enter your birth year:"))
c=a-b
print("subtraction=",c)



p=int(input("enter the value of p"))
r=int(input("enter the value of r"))
t=int(input("enter the value of t"))
si=(p*r*t)/100
print("si=",si)


pi=3.14
r=int(input("enter the value of r"))
area=pi*r*r
print("area of circle=",area)



number=9
if number%2 == 0:
    print(number,"even number")
else:
    print(number,"even number")


# Homework

#Q1
name=input("enter your name: ")
age=int(input("enter your age: "))

print(f"hello {name},your age is {age} years")


#Q2

length=float(input("enter length: "))
breadth=float(input("enter breadth: "))

perimeter=2*(length+breadth)
print(perimeter)


#Q3

kilometers=float(input("enter distance in kilometers: "))
meters=kilometers*1000
centimeters=kilometers*100000
print(f"distance in meters: {meters}")
print(f"distance in centimeters: {centimeters}")

#Q4

price1=float(input("enter price of item 1: "))
price2=float(input("enter price of item 2: "))
price3=float(input("enter price of item 3: "))

total_price=price1+price2+price3
print(f"total price: {total_price}")


#Q5

hours=float(input("enter hours: "))
minutes=hours*60
seconds=hours*3600

print(f"minutes: {minutes}")
print(f"seconds: {seconds}")


#Q6


base=float(input("enter base of the triangle: "))
height=float(input("enter height of the triangle: "))

area=(base*height)/2
print(f"area of the triangle: {area}")



#Q7

no=float(input("enter a number: "))
double=no*2
triple=no*3
print(f"double of the number: {double}")
print(f"triple of the number: {triple}")

#Q8

noOfDays=int(input("enter number of days: "))
seconds=noOfDays*24*60*60
print(f"number of seconds in {noOfDays} days: {seconds}")


#Q9

rupees=float(input("enter amount in rupees: "))
paise=rupees*100
print(f"amount in paise: {paise}")


#Q10

boys=int(input("enter number of boys: "))
girls=int(input("enter number of girls: "))
total_students=boys+girls
print(f"total number of students: {total_students}")




