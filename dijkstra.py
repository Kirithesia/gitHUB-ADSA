# Experiment 9: Dijkstra's Algorithm
# Single Source Shortest Path

INF = float('inf')


def dijkstra(graph, source):
    n = len(graph)

    # Initialize distance and visited arrays
    distance = [INF] * n
    visited = [False] * n

    # Distance from source to itself is 0
    distance[source] = 0

    for _ in range(n):

        # Find unvisited vertex with minimum distance
        u = -1
        minimum = INF

        for i in range(n):
            if not visited[i] and distance[i] < minimum:
                minimum = distance[i]
                u = i

        # If no reachable vertex is found
        if u == -1:
            break

        # Mark vertex as visited
        visited[u] = True

        # Update distances of adjacent vertices
        for v in range(n):
            if (not visited[v] and
                    graph[u][v] != 0 and
                    distance[u] + graph[u][v] < distance[v]):

                distance[v] = distance[u] + graph[u][v]

    return distance


# Example graph
graph = [
    [0, 4, 1, 0, 0],
    [4, 0, 2, 5, 0],
    [1, 2, 0, 8, 10],
    [0, 5, 8, 0, 2],
    [0, 0, 10, 2, 0]
]

source = 0

distance = dijkstra(graph, source)

# Display shortest distances
print("Shortest distances from vertex", source)

for i in range(len(distance)):
    if distance[i] == INF:
        print(f"Vertex {i}: INF")
    else:
        print(f"Vertex {i}: {distance[i]}")
