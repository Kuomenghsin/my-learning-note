#!/usr/bin/env python
# coding: utf-8

# In[29]:


arr = [5,9,7,6,4,8,11,13]
def quick_sort(list): #extra-place
    small = []
    big = []
    point = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                small.append(i)
        return small    
quick_sort(arr)


# In[30]:


arr = [5,9,7,6,4,8,11,13]
def quick_sort(list): #extra-place
    small = []
    big = []
    point = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                small.append(i)
            elif i > key: #比key值大的數
                big.append(i)    
    return small + big 

    
quick_sort(arr)


# In[31]:


def quick_sort(list): #extra-place
    small = []
    big = []
    point = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                small.append(i)
            elif i > key: #比key值大的數
                big.append(i)    
            else:
                point.append(i)
    return small + point + big

    
quick_sort(arr)


# In[32]:


def quick_sort(list): #extra-place
    small = []
    big = []
    point = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                small.append(i)
            elif i > key: #比key值大的數
                big.append(i)    
            else:
                point.append(i)
                
                
    small = quick_sort(small)     
    return small + point + big 

    
quick_sort(arr)


# In[33]:


def quick_sort(list): #extra-place
    small = []
    big = []
    point = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                small.append(i)
            elif i > key: #比key值大的數
                big.append(i)    
            else:
                point.append(i)
                
                
    small = quick_sort(small)   
    big  = quick_sort(big)
    return small + point  + big

    
quick_sort(arr)


# In[ ]:


def quick_sort(list): #extra-place
    smaller = []
    bigger = []
    keylist = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                smaller.append(i)
            elif i > key: #比key值大的數
                bigger.append(i)
            else:
                keylist.append(i)

    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)
    return smaller + keylist + bigger

