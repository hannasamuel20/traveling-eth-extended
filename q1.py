from graph_data import unweighted_graph
from copy import deepcopy
from collections import deque

class TravelingEthiopia:
    
    def __init__(self,graph):
        self.graph = graph
    
    def search(self,start,goal,strategy):
        visited = set()
        def dfs(start,path):
            if start in visited:
                return []
            path.append(start)
            visited.add(start)
            if(start == goal):
                return deepcopy(path)
            for neigh in self.graph[start]:
                path_found = dfs(neigh,path)
                if(path_found):
                    return path_found
            path.pop()
        def bfs(start):
            q = deque()
            q.append([start])
            visited.add(start)
            while q:
                curr_path = q.popleft()
                if(curr_path[-1] == goal):
                    return curr_path
                for neigh in self.graph[curr_path[-1]]:
                    if neigh not in visited:
                        visited.add(neigh)
                        new_path = deepcopy(curr_path)
                        new_path.append(neigh)
                        q.append(new_path)
            return []
        if(strategy == "DFS"):
            return dfs(start,[])
        elif strategy == "BFS":
            return bfs(start)
if __name__ == "__main__":             
    te = TravelingEthiopia(unweighted_graph)
    print(te.search("Addis Ababa","Debre Tabor","BFS"))
           


