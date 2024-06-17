from collections import deque
import random


class Node:
    def __init__(self, operation):
        self.final_value = 0
        self.inherited_value = float('-inf')  # Use float('-inf') for minimum inherited value
        self.random_number = random.randint(1, 100)
        self.level = 0

        self.child = None
        self.parent = None

        self.operation_to_perform = operation

    def set_child(self, child):
        self.child = child

    def set_parent(self, parent):
        self.parent = parent

    def set_inherited(self, inherited_value):
        self.inherited_value = max(self.inherited_value, inherited_value)

    def set_level(self, level):
        self.level = self.level + level

    def set_final(self):
        if self.operation_to_perform == '+':
            self.final_value = self.inherited_value + self.random_number
        elif self.operation_to_perform == '-':
            self.final_value = self.inherited_value - self.random_number
        elif self.operation_to_perform == '*':
            self.final_value = self.inherited_value * self.random_number
        elif self.operation_to_perform == '/':
            self.final_value = self.inherited_value // self.random_number
        elif self.operation_to_perform == '%':
            self.final_value = self.inherited_value % self.random_number

    def get_level(self):
        return self.level

    def get_final(self):
        return self.final_value

def myFunctionModule(input_val: int):
    f = open('input.txt', 'r')

    V, E = map(int, f.readline().split())

    adj = [[] for _ in range(V + 1)]  # Adjacency list
    mp = {}  # Mapping of node number to Node object

    for i in range(1, V + 1):
        node, operation = f.readline().split()
        node = int(node)
        operation = str(operation)

        temp = Node(operation)
        mp[node] = temp

    # Indegree
    indegree = [0] * (V + 1)

    for i in range(1, V ):
        a, b = map(int, f.readline().split())
        adj[a].append(b)

        parent = mp[a]
        child = mp[b]

        parent.set_child(child)
        child.set_parent(parent)

        indegree[b] += 1

    queue = deque()
    max_level = 1
    ans_nodes = []

    for node in range(1, V + 1):
        if indegree[node] == 0:
            queue.append(node)
            mp[node].set_inherited(input_val)
            mp[node].set_level(1)
            ans_nodes.append(node)

    while queue:
        node = queue.popleft()

        mp[node].set_final()

        for child in adj[node]:
            mp[child].set_inherited(mp[node].get_final())
            mp[child].set_level(mp[node].get_level())

            if mp[child].get_level() > max_level:
                max_level = mp[child].get_level()
                ans_nodes = [child]
            elif mp[child].get_level() == max_level:
                ans_nodes.append(child)

            indegree[child] -= 1

            if indegree[child] == 0:
                queue.append(child)

    print(f"MaxLevel: {max_level}")
    for node in ans_nodes:
        print(f"Node number: {node}, Final Value: {mp[node].get_final()}" )

    return "Done!!"

