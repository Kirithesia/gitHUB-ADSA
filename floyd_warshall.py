# Experiment 10: Floyd-Warshall Algorithm
# All-Pairs Shortest Path

INF = float('inf')


def floyd_warshall(graph):
    n = len(graph)

    # Create distance matrix
    dist = [row[:] for row in graph]

    # Find all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):

                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    # Display shortest distance matrix
    print("Shortest Distance Matrix:")

    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

    return dist


# Example graph
graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

floyd_warshall(graph)
