graph = {
    '1': ['2', '3', '4', '5'],
    '3': ['6'],
    '4': ['7'],
    '2': ['6'],
    '5': ['7'],
    '6': ['8'],
    '7': ['8'],
    '8': []
}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '1')  # function calling
# function calling
