from graph_data import weighted_graph
from copy import deepcopy
from collections import deque
import heapq

# Question 2
class TravelingEthiopia:
    
    def __init__(self,graph):
        self.graph = graph

    # For Question 2.2 "Addis Ababa -> Lalibela" (it can also generalize for other source and destinations)
    def dijkstra(self,start,goal):
        min_heap = []
        visited = set()
        heapq.heappush(min_heap,(0, [start]))
        while min_heap:
            dist,curr_path = heapq.heappop(min_heap)
            last_city = curr_path[-1]
            visited.add(last_city)
            if last_city == goal:
                return (curr_path,dist)
            for neigh,next_dist in self.graph[last_city]:
                if neigh not in visited:
                    new_path = deepcopy(curr_path)
                    new_path.append(neigh)
                    heapq.heappush(min_heap,(dist+next_dist,new_path))
        return ([],-1)

    # For Question 2.3 "Addis Ababa" -> MULTIPLE_CITIES
    def customized_dijkstra(self, start, goal_states):
        min_heap = []
        heapq.heappush(min_heap,(0, [start], set(), 0))
        while min_heap:
            dist, curr_path, visited_cities, found_goals = heapq.heappop(min_heap)
            last_city = curr_path[-1]
            visited_cities.add(last_city)
            if last_city in goal_states:
                found_goals+=1
            if found_goals ==  len(goal_states):
                return (curr_path, dist)
            for neigh, next_dist in self.graph[last_city]:
                if neigh not in visited_cities:
                    new_path = deepcopy(curr_path)
                    new_visited = deepcopy(visited_cities)
                    new_path.append(neigh)
                    heapq.heappush(min_heap,(dist+next_dist,new_path,new_visited,found_goals))
        return ([], -1)
        
if __name__ == "__main__":
    te = TravelingEthiopia(weighted_graph)
    print(te.dijkstra("Addisababa", "Lalibela"))
    print(te.customized_dijkstra("Addisababa", ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sofoumer", "Arbaminch"]))



    