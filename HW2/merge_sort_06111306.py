#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):

    #MergeSort
    def merge_sort(self, nums):
        self.nums = nums
        num1=nums[:len(nums)//2]
        num2=nums[len(nums)//2:]
        num3=[]
        
        self.divide_sort(num1, len(num1)-1)
        self.divide_sort(num2, len(num2)-1)
        self.combine(len(num1),len(num2))
        
        return nums
    
    #Divide
    def divide_sort(self,num,size):
        for i in range(size-1):
            for base in range(size-1-i):
                min=base
                for compare in range(size):
                    compare=base+1
                    if num[compare]<num[min]:
                        min=compare
                    
                    temp=num[min]
                    num[min]=num[base]
                    num[base]=temp
            
    #Combine
    def combine(self,size1,size2):
        arg1=0
        arg2=0              
        num1.append(999)
        num2.append(999)

        for arg3 in range(size1+size2):
            if num1[arg1]<num2[arg2]:
                num3.append(num1[arg1])
                arg1+=1
            else:
                num3.append(num2[arg2])
                arg2+=1
                
            

                
#Output
output = Solution().merge_sort([2,5,6,8,7,9])
output

