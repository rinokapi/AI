graph = {
  1 : [4, 2],
  4 : [3],
  2 : [5, 7, 8],
  3 : [10, 9],
  5 : [6],
  7 : [],
  8 : [],
  10 : [],
  9 : [],
  6 : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 1)