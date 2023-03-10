import heapq

def a_star(grid, start, end):
    # Helper function to calculate the heuristic cost
    def heuristic(a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    # Create a priority queue to store the next steps to explore
    queue = []
    heapq.heappush(queue, (0, start))

    # Create a dictionary to store the cost of each point
    cost = {start: 0}

    # Create a dictionary to store the parent of each point
    parent = {start: None}

    # Create a set to store the visited points
    visited = set()

    # While there are points to explore
    while queue:
        # Get the point with the lowest cost
        current = heapq.heappop(queue)[1]

        # If we have reached the end point, construct the path
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        # Mark the current point as visited
        visited.add(current)

        # Explore the neighboring points
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + i, current[1] + j
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                # Calculate the new cost
                new_cost = cost[current] + 1

                # If the neighbor has not been visited or the new cost is lower
                if neighbor not in cost or new_cost < cost[neighbor]:
                    # Update the cost and parent of the neighbor
                    cost[neighbor] = new_cost
                    priority = new_cost + heuristic(end, neighbor)
                    heapq.heappush(queue, (priority, neighbor))
                    parent[neighbor] = current
    return None

# Example usage:
grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
start = (0, 0)
end = (7, 6)
path = a_star(grid, start, end)
print(path)