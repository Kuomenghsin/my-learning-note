Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        """
        :rtype: dict
        """
