# Prim's Algorithm - Minimum Spanning Tree

def min_key(key, mst_set, V):
    minimum = float('inf')
    min_index = -1

    for v in range(V):
        if not mst_set[v] and key[v] < minimum:
            minimum = key[v]
            min_index = v

    return min_index


def prim_mst(graph):
    V = len(graph)

    parent = [-1] * V
    key = [float('inf')] * V
    mst_set = [False] * V

    # Start from vertex 0
    key[0] = 0

    for _ in range(V - 1):
        # Pick minimum key vertex
        u = min_key(key, mst_set, V)

        # Add vertex to MST
        mst_set[u] = True

        # Update adjacent vertices
        for v in range(V):
            if graph[u][v] != 0 and not mst_set[v]:
                if graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u

    # Print MST
    print("Edge\tWeight")

    total_weight = 0

    for i in range(1, V):
        print(f"{parent[i]} - {i}\t{graph[i][parent[i]]}")
        total_weight += graph[i][parent[i]]

    print("Total Weight:", total_weight)


# Example graph represented as an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)
