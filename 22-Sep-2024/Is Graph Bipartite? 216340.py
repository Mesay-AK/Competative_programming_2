# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        white = 0
        black = -1
        grey = 1

        g = [white for i in range(len(graph))]

        def dfs(node):
            track = True
            for k in graph[node]:


                if g[node] == g[k]:
                    return False
        
                elif g[k] == white:
                    if g[node] == black:
                        g[k] = grey
                    elif g[node] == grey:
                        g[k] = black
                    track = track and dfs(k)

            return track


        result = True

        for i in range(len(g)):
            if g[i] == white:
                g[i] = grey
                result = result and dfs(i) 
               


        return result



                
                    
                    






        
