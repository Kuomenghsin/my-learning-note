#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        #MD5加密
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
              
        #找出index
        index = int(h, 16)%self.capacity
        
        #空的-->直接加入
        if self.data[index]==None:
            self.data[index]=ListNode(h)
        
            
        #有東西-->加入下一個
        else:
            temp=ListNode(h)
            now=self.data[index]
            while now.next != None:
                now = now.next
                now.next=temp
        print('AddIndex:',index)
                
        """
        :type key: int
        :rtype: None
        """


    def remove(self, key):
        #MD5加密
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        index = int(h, 16)%self.capacity
        
        
        #有東西
        delVal = self.data[index]
        if self.data[index]!=None:
            #是要刪的值            
            if delVal == ListNode(h):
                delVal = None
                print('DelIndex:',index)
            else:
                self.data[index]=self.data[index].next
                print('Next Index')
        #沒東西      
        else:
            delVal=delVal.next
            
        
                
        """
        :type key: int
        :rtype: None
        """
    
    def contains(self, key):
        #MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        
        index = int(h , 16)%self.capacity
        
        if self.data[index] != None:
            target = self.data[index]
            
            while target.next != None:
                target = target.next
                if target.val == h:
                    break

            if target.val == h:
                return True
            else:
                return False
        else:
            return False
        
        """
        :type key: int
        :rtype: bool(True or False)
        """

