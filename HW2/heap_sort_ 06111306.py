#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution():


    def heap_sort(self, nums):
        self.nums = nums
        self.heapSort(nums)
        return nums
        
    def toHeap(self,arr, n, i): #堆積size = n
        bigest = i  # 子樹根初始值 index = i
        L = 2*i + 1     # (左子節點) = 2*i + 1 由左子數計算樹根位址i
        R = 2*i + 2     # (右子節點) = 2*i + 2 由右子數計算樹根位址i
  
        # 左子節點存在而且大於父節點
        if L < n and arr[i] < arr[L]: 
            bigest = L  
  
        # 右子節點存在而且大於父節點 
        if R < n and arr[bigest] < arr[R]: 
            bigest = R 
  
        #   更換父節點 
        if bigest != i: 
            arr[i],arr[bigest] = arr[bigest],arr[i]  # 兩兩交換 
  
            # 最後堆積樹根 
            self.toHeap(arr, n, bigest)

    # 主程式根據串列sort
    def heapSort(self,arr): 
        n = len(arr) #串列大小
  
        # 建立maxheap串列(父節點永遠大於子節點) 
        for i in range(n, -1, -1):
            self.toHeap(arr, n, i) 
  
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]   # 兩兩交換
            self.toHeap(arr, i, 0) 
  
output=Solution().heap_sort([ 2, 4 ,7, 1, 21,-3, 64, 12, 11, 15, 4, 7, 8])
output


# In[ ]:




