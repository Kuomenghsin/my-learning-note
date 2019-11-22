#!/usr/bin/env python
# coding: utf-8

# In[16]:


class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    #新增
    def insert(self,root,val):
        #root空
         if root == None:
            N_node = TreeNode(val)
            return N_node
        #加入數值=root
        else root.val == val:
            root.left = TreeNode(val)
            N_node.left = root.left
            root.left = N_node
            return N_node
            
        #加入數值小於root的情況
        if root.val > val and root != None and root.val != val:
            # 左邊沒有子數，直接加入
            if root.left == None:
                N_node = TreeNode(val)
                root.left =N_node
                return N_node
            else:
                #把左子樹(root.left)當作root
                #並遞迴直到找出val應加入的位置
                return Solution().insert(root.left,val) 
        
        #加入數值大於root的情況
        if root.val < val and root != None and root.val != val:
            if root.right == None:
                N_node=TreeNode(val)
                root.right = N_node
                return N_node
                
            else:
                #把右子樹(root.right)當作root
                #並遞迴直到找出val應加入的位置
                ruturn Solution().insert(root.right,val)
                
    #搜尋
    def search(self,root,target):
        #目標小於root
        if target < root.val:
            return Solution().search(self,root.left,target)
        #目標大於root
        elif target > root.val:
            return Solution().search(self,root.right,target)
        #目標等於root
        elif target == root.val:
            return root
        #找不到
        else:
            return None

    #左邊最大function
    def maxVal(self,root)
        Max = root
        while(root.right != None):
            Max = Max.right
            
        return Max
        
    #刪除(正確)
    def delete(self,root,target):
        #找到目標
        if root.val = target: 
            root.val = None
            return root
        #欲刪除的目標在右邊
        if target > root.val:
            root.right = Solution().delete(root.right, target) 
        #欲刪除的目標在左邊
        elif target < root.val:
            root.left = Solution().delete(root.left, target)
            
        else:
            #若沒有子樹或只有一個
            if root.right != None:
                temp = root.left
                root = None
                return temp
            
            else root.left != None:
                tem = root.right
                root = None
                return temp
            #左右皆有子樹，找左邊最大補
            tem = maxVal(root.left)
            
            #複製他到刪除的node
            root.val = temp.val
            
            #刪掉原本左邊最大的節點
            root.left = Solution().delete(root.left, temp.val)
        return root
            
            
        
    
                
    #修改
    def modify(self,root,target,val):
        if target != val:  
            #透過前面的insert加入欲輸入的值
            Solution().insert(root,val)
            #透過刪除刪掉原先的值
            return Solution().delete(root,target)
        else:
            return root
            
            
            
    
            
        
                


# In[ ]:




