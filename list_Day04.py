#Q1
list=[1,2,3,4,5]
print(list)
print(type(list))

a=(1,2,3,4,5)
print(a)
print(type(a))


set1={2,6,8,9,7,5}
print(set1)
print(type(set1))

dictionary={"name":"akash","age":19}
print(dictionary)
print(type(dictionary))

#Q2
list=[1,2,3,4,4,4,5]
list.reverse()
print(list)
print(list.index(3))
print("count of 4 =",list.count(4))
list2=[6,4,8,6,2,1,4,9,11,5]
print(list2)
list2.sort()
print(list2)


list=[1,2,3,3,2,3,2,1,2,3,2,,4,4,4,5]
data=[]
for i in num:
    if i not in data:
        data.append(i)
print("Actual list:",num)
print("After removing duplicate:",data)   

#Q3
# find second largest number
number=[12,34,35,64,75,68,39,45,79,35]
maximum=second_largest=float('-inf')
for i in number:
    if i>maximum:
        secomd_largest=maximum
        maximum=i
    elif i>second_largest and i!=maximum:
        second_largest=i
print("second largest value:",second_largest)

#Q4 leet code two sum questions
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    return[i,j]


















