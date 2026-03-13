#Q1
def solveMeFirst(a,b):
	return a + b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

#Q2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

    #Q3
    #!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return [alice, bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

 #Q4
 #!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)  

#Q5
def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:8]
        else:
            return s[:8]
    else:  # PM case
        if s[:2] == "12":
            return s[:8]
        else:
            hour = str(int(s[:2]) + 12)
            return hour + s[2:8]


s = input()
print(timeConversion(s))

#Q6 Palindrome lead code Q9    
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        
        if s == s[::-1]:
            return True
        else:
            return False
 #Q7
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

