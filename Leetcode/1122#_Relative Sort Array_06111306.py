class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import defaultdict
        hmap = defaultdict(int)
        visited = set()
        for elt in arr1:
            hmap[elt] +=1
            
        ret_list = []
        
        for elt in arr2:
            ret_list.extend([elt]*hmap[elt])
            visited.add(elt)
        
        unvisited = sorted(set(hmap.keys()).difference(visited))
        for elt in unvisited:
            ret_list.extend([elt]*hmap[elt])
        
        return ret_list
