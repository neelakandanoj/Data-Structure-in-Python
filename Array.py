# Problem 1
"""Input: arr[] = {0, -1, 2, -3, 1}, target = -2
Output: True
Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2


Input: arr[] = {1, -2, 1, 0, 5}, target = 0
Output: False
There is no pair with sum equals to given target.
"""
l=list(map(int,input().split(',')))
target=int(input("Enter the target to sum: "))

size=len(l)
def twoSum(l,size):
 for i in range(size):
   for j in range(i+1,size):
     if l[i]+l[j]==target:
        return (i,j);
 return False;

twoSum(l,size)

# --------------------------------------------------------------------------------------------------------------------------------------------
"""Input: n=7 , array[]={1, 2, 3, 6, 3, 6, 1}
Output: 1, 3, 6
Explanation: The numbers 1 , 3 and 6 appears more than once in the array.


Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3
Explanation: The number 3 appears more than once in the array.
"""
# num=[1, 2, 3, 6, 3, 6, 1]
num="hello world hello"
frequency={}
duplicate=[]

for i in num:
  if i in frequency:
    frequency[i]+= 1
  else:
    frequency[i]=1

for num, count in frequency.items():
  if count>1:
    duplicate.append(num)

print(duplicate)

