# Q1
def q1(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Q2
def q2(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

# Q3
def q3(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

# Q4
def q4(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)

# Q5
def q5(n):
    for i in range(1, n+1):
        print(i)

# Q6
def q6(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even:", even, "Odd:", odd)

# Q7
def q7(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print(rev)

# Q8
def q8(n):
    if n <= 1:
        print("Not Prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")

# Q9
def q9(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    print(s)

# Q10
def q10(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

# Q11
def q11(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")

# Q12
def q12(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    print(largest)

# Q13
def q13(s):
    count = 0
    for i in s.lower():
        if i in "aeiou":
            count += 1
    print(count)

# Q14
def q14(age):
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")

# Q15
def q15(lst):
    lst = list(set(lst))
    lst.sort()
    print(lst[-2])

# Q16
def q16(n):
    s = 0
    for i in range(1, n+1):
        s += i
    print(s)

# Q17
def q17(p):
    if len(p) >= 8:
        if any(c.isdigit() for c in p):
            print("Strong Password")
        else:
            print("Add Numbers")
    else:
        print("Weak Password")

# Q18
def q18(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

# Q19
def q19(n):
    if n % 3 == 0 and n % 5 == 0:
        print("Divisible")
    else:
        print("Not Divisible")

# Q20
def q20(sentence):
    words = sentence.split()
    print(len(words))

# Q21
def q21(n):
    if n >= 1000:
        print(str(n//1000) + "K")
    else:
        print(n)

# Q22
def q22(v):
    if v >= 1000000:
        print(str(v//1000000) + "M")
    elif v >= 1000:
        print(str(v//1000) + "K")
    else:
        print(v)

# Q23
def q23(time):
    if time < 10:
        print("Preparing")
    elif time < 30:
        print("Out for Delivery")
    else:
        print("Delivered")

# Q24
def q24(prices):
    total = 0
    for p in prices:
        total += p
    print(total)

# Q25
def q25(balance, amount):
    if balance >= amount:
        print("Payment Successful")
    else:
        print("Insufficient Balance")

# Q26
def q26(minutes):
    print(minutes/60, "hours")

# Q27
def q27(base, traffic):
    if traffic == "high":
        print(base * 1.5)
    else:
        print(base)

# Q28
def q28(minutes):
    print("Last seen", minutes, "minutes ago")

# Q29
def q29(level):
    if level > 70:
        print("Full")
    elif level > 30:
        print("Medium")
    else:
        print("Low")

# Q30
def q30(count):
    if count >= 10000:
        print("Goal Completed")
    else:
        print("Keep Walking")

# Q31
def q31(n):
    while n > 0:
        print(n)
        n -= 1

# Q32
def q32(amount):
    if amount > 1000:
        print(amount * 0.1)
    else:
        print(amount * 0.05)

# Q33
def q33(distance):
    print(distance * 2, "hours")

# Q34
def q34(temp):
    if temp > 30:
        print("T-shirt")
    elif temp > 20:
        print("Jacket")
    else:
        print("Sweater")

# Q35
def q35(percent):
    if percent >= 75:
        print("Allowed")
    else:
        print("Shortage")

# Q36
def q36(amount):
    if amount > 50000:
        print("Fraud Alert")
    else:
        print("Normal")

# Q37
def q37(used, total):
    if used/total > 0.8:
        print("High Usage")

# Q38
def q38(seats):
    if seats > 0:
        print("Available")
    else:
        print("Waiting List")

# Q39
def q39(distance, speed):
    print(distance/speed, "hours")

# Q40
def q40(stars):
    print("Rating:", stars, "/5")

# Q41
def q41(amount):
    print(amount * 0.1)

# Q42
def q42(used, total):
    if used/total > 0.9:
        print("Storage Almost Full")

# Q43
def q43(h):
    if h > 70:
        print("Healthy")
    elif h > 30:
        print("Low")
    else:
        print("Critical")

# Q44
def q44(speed):
    if speed > 80:
        print("Speed Limit Exceeded")

# Q45
def q45(old, new):
    if new > old:
        print("Growth")
    elif new == old:
        print("No Change")
    else:
        print("Decline")

# Q46
def q46(temp):
    if temp > 85:
        print("Overheating")

# Q47
def q47(days):
    print("Streak:", days)

# Q48
def q48(p, r, t):
    print((p*r*t)/100)

# Q49
def q49(amount):
    gst = amount * 0.18
    print(amount + gst)

# Q50
def q50(lst):
    count = 0
    for i in lst:
        if i == "present":
            count += 1
    print(count)



# Function Calls

q1(10)
q2(10, 20, 5)
q3(-3)
q4(5)
q5(5)
q6([1,2,3,4,5,6])
q7(1234)
q8(7)
q9(123)
q10(5)
q11(2024)
q12([3,7,2,9,5])
q13("Hello World")
q14(20)
q15([1,5,3,9,7])
q16(10)
q17("pass1234")
q18(5)
q19(15)
q20("Python is easy to learn")
q21(12000)
q22(560000)
q23(15)
q24([200,300,150])
q25(5000,2000)
q26(180)
q27(200,"high")
q28(10)
q29(50)
q30(8000)
q31(5)
q32(1200)
q33(10)
q34(25)
q35(80)
q36(60000)
q37(9,10)
q38(0)
q39(100,50)
q40(4)
q41(300)
q42(95,100)
q43(40)
q44(90)
q45(1000,1200)
q46(90)
q47(15)
q48(1000,5,2)
q49(500)
q50(["present","absent","present","present"])