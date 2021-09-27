# Using a Python dictionary to act as an adjacency list
graph = {
  1 : [4, 2],
  4 : [3],
  3 : [10, 9, 2],
  10 : [],
  9 : [],
  2 : [8, 7, 5],
  8 : [7],
  7 : [5],
  5 : [6],
  6 : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 1)

# 1
# 4
# 3
# 10
# 9
# 2
# 8
# 7
# 5
# 6
