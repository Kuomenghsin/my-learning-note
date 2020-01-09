#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict

class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        #Create a new list
        queue=[]
        lv1=[]
        lv2=[]
        lv3=[]
        queue.append(s)
        
        #Level1      
        for i in range(len(self.graph[s])):
            queue.append(self.graph[s][i])
            lv1.append(self.graph[s][i])
      
        for i in range(len(self.graph)):
            if s in self.graph[i] and i not in queue:
                queue.append(i)
                lv1.append(i)
        print('Level1:',lv1)        
        #Level2
        for i in range(len(self.graph[s])):
            numInS = self.graph[s][i]
            for j in range(len(self.graph[numInS])):
#                 print(self.graph[numInS])
#                 print('AddNum:', self.graph[numInS][j])
                if self.graph[numInS][j] not in queue:
                    queue.append(self.graph[numInS][j])
                    lv2.append(self.graph[numInS][j])
        print('Level2:',lv2)
        #Level3
        for i in range(len(lv2)):
            numInLv2=lv2[i]
            for j in range(len(self.graph[numInLv2])):
                if self.graph[numInLv2][j] not in queue:
                    queue.append(self.graph[numInLv2][j])
                    lv3.append(self.graph[numInLv2][j])
        print('Level3:', lv3)
        
        return queue
    
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        #Define a empty list 
        queue=[]
        queue.append(s)
                
        def DFSfn(x, queue=[]):
            #Define search point
            time=0
            searchPoint = x
            #print('Origin Search Point:', searchPoint)
    
            #Check if not empty    
            if self.graph[searchPoint] != []:
                #Define next search point s[].pop()
                #print('Search queue:', self.graph[searchPoint])
                
                #Check if number already in queue
                if self.graph[searchPoint][len(self.graph[searchPoint])-1] not in queue:
                    searchPoint = self.graph[searchPoint].pop()
                else:
                    self.graph[searchPoint].pop()
                    
                if searchPoint not in queue:
                    queue.append(searchPoint)
                    #print('Current queue:', queue)
                    #print('Search Point.next:', searchPoint)
                    DFSfn(searchPoint, queue) 
                else:
                    DFSfn(searchPoint, queue)
            
            #If empty, back to the previous search point
            else:
                for i in range(len(self.graph)):
                    if self.graph[i] != []:
                        searchPoint = queue[queue.index(searchPoint)-1]
                        DFSfn(searchPoint, queue)
                    
              
                          
        DFSfn(s, queue)
            
        return queue

