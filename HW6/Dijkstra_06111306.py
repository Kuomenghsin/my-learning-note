#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0]*vertices for i in range(vertices)] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """       
        self.graph[u][v] = w
        
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
           
    def Kruskal(self):
        """
        :rtype: dict
        """
        visited = []
        num = self.V
        ans = {}
        
        
#         def fn ():
#             for c in range(self.V):
#                 for d in range(self.V):
#                     if self.graph[c][d] != 0 and self.graph[c][d] <= minPath:
#                         minPath = self.graph[c][d]
#                         if c not in visited:
#                             visited.append(c)
#                         if d not in visited:
#                             visited.append(d)
#                         self.graph[c][d] = 0
#                         print(c, '-', d, ':', minPath)
                        
        while len(visited) < self.V:
            minPath = 1000
            print(visited)
            for a in range(num):
                for b in range(num):
                    if self.graph[a][b] != 0 and self.graph[a][b] < minPath:
                        minPath = self.graph[a][b]
                        
            print(minPath)
            
            for c in range(self.V):
                for d in range(self.V):
                    if self.graph[c][d] != 0 and self.graph[c][d] <= minPath:
                        if c not in visited or d not in visited:
                            minPath = self.graph[c][d]
                            if c not in visited:
                                visited.append(c)
                            if d not in visited:
                                visited.append(d)
                            self.graph[c][d] = 0
                            ans['%s-%s' %(c,d)] = minPath
                            
                        else:
                            self.graph[c][d] = 0
                    
        return ans
    

