from graph_data import adversarial_graph,reward_map

class MiniMax:
    def __init__(self,graph,reward):
        self.graph = graph
        self.reward = reward
    
    def maximize_reward(self,node):
        maximum = float("-inf")
        for neigh in self.graph[node]:
            maximum = max(maximum,self.start_game(neigh,False))
        return maximum

    def minimize_reward(self,node):
        minimum = float("inf")
        for neigh in self.graph[node]:
            minimum = min(minimum,self.start_game(neigh,True))
        return minimum

    def start_game(self, node, is_agents_turn):
        if node not in self.graph:
            return self.reward[node]
        if is_agents_turn:
            return self.maximize_reward(node)
        return self.minimize_reward(node)

mm = MiniMax(adversarial_graph,reward_map)

# "True" mean our agent gets to go first
print(mm.start_game("Addis Ababa", True))        



