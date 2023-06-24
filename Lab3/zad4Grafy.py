import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    path = [None] * n
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, path


if __name__ == "__main__":
    # przykładowy graf jako lista sąsiedztwa (indeks to numer wierzchołka, a krotki to pary (sąsiad, waga))
    graph = [
        [(1, 1), (2, 2)],
        [(0, 1), (2, 3), (3, 7)],
        [(0, 2), (1, 3), (3, 1), (4, 5)],
        [(1, 7), (2, 1), (4, 2)],
        [(2, 5), (3, 2)]
    ]

    distances, path = dijkstra(graph, 0)
    print("Distances:", distances)
    print("Path:", path)
