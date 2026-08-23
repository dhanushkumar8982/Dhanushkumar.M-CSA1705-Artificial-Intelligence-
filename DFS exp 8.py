# Python program to implement DFS

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = set()


def dfs(graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor)


# Get starting node from user
start = input("Enter starting node: ").upper()

print("DFS Traversal:")
dfs(graph, start)
