
from graph_data import weighted_graph,heuristics
from copy import deepcopy
from collections import deque
import heapq

class TravelingEthiopia:
    
    def __init__(self,graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics
    # For questions 3 "Addis Ababa" -> "Moyale" can generalize to other source and destinations
    def a_star(self,start,goal):
        min_heap = []
        visited = set()
        heapq.heappush(min_heap,(heuristics[start],0, [start]))
        while min_heap:
            _ , backward_cost, curr_path = heapq.heappop(min_heap)
            last_city = curr_path[-1]
            visited.add(last_city)
            if(last_city == goal):
                return (curr_path,backward_cost)
            for neigh,weight in self.graph[last_city]:
                if neigh not in visited:
                    new_path = deepcopy(curr_path)
                    new_path.append(neigh)
                    new_backward_cost = weight+backward_cost
                    heapq.heappush(min_heap,(heuristics[neigh]+new_backward_cost,new_backward_cost,new_path))
        return ([],-1)

if __name__ == "__main__":
    te = TravelingEthiopia(weighted_graph,heuristics)
    print(te.a_star("Addis Ababa","Moyale"))

    