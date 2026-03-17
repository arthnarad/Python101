# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)

# add()


# with argument
# def addition(a,b):
#     x=a+b
#     print("Addition = ",x)
# addition(10,30)
# with argument with return
#def addition2(a,b):
#   return a+b
#print(addition2(50,60))

def linear_search(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i 
        return -1
list=[10,20,30,40,50] 
target = int(input("Enter any  number:"))
index=linear_search(list,target)
print("Elemental found at index :",index)



def linear_search(list,target):
   i=0
   while i<len(list):
      if list[i]==target:
          return i
      i+=1
      return -1  
list=[10,20,30,40,50] 
target = int(input("Enter any  number:"))
index=linear_search(list,target)
print("Elemental found at index :",index)


list=[10,20,30,40,50] 
# if else condition
target=30
if target in list:
    print("found at index:",list.index(target))
else :
    print("not found")



# LeetCode

# 704.Binary Search
class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    


# 268. Missing Number

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum