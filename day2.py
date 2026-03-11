a=10
b=20
c=a+b
print("addition= ",c)

#print nummbers 1 to 30
for i in range(1,31):
    if i %2==0:
        print(i,"even number")
    if i %2!=0:
        print(i,"odd number")

#largest number
a,b,c=10,20,30
if a>=b and c>=b:
    print("a is largest")
if b>=a and b>=c:
    print("b is largest")
if c>=b and c>=a:
    print("c is largest")
    
# +ve or -ve number
number = 7
if number>0:
    print("postive num")
elif number<0:
    print("neegative num")
else:
    print("number is zero")     
    
# sum of all natrul nos.

n=5  
sum = 5
for i in range (1,n+1):
      sum=sum+i
print(sum)


# find the factorial
number = 6
fact = 1
for i in range(1,number+1):
     fact = fact*i 
print(fact)     



#HomeWork

#Q1

for i in range(1, 21):  
    print("Table of", i)
    
    for j in range(1, 11):   
        print(i, "x", j, "=", i*j)
        
    print() 


#Q2

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


#Q3

num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")




#Q4


num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime number")
else:
    print("Not Prime")



#Q5


num = int(input("Enter a number: "))

temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num // 10

if temp == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")



#Q6

text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome")