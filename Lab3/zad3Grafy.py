import numpy as np

from collections import deque


def create_graph():
    graph_type = input(
        "Podaj typ grafu (skierowany, nieskierowany, ważony): ").lower()
    vertices = int(input("Podaj ilość wierzchołków: "))
    edges = int(input("Podaj ilość krawędzi: "))

    adjacency_list = {i: deque() for i in range(vertices)}
    adjacency_matrix = np.zeros((vertices, vertices))

    for _ in range(edges):
        edge = list(
            map(int, input("Podaj krawędź jako parę wierzchołków (np. '0 1'): ").split()))

        if graph_type == "ważony":
            weight = float(input("Podaj wagę dla tej krawędzi: "))
            adjacency_matrix[edge[0]][edge[1]] = weight
            adjacency_list[edge[0]].append((edge[1], weight))
        else:
            adjacency_matrix[edge[0]][edge[1]] = 1
            adjacency_list[edge[0]].append(edge[1])

        if graph_type == "nieskierowany":
            if graph_type == "ważony":
                adjacency_matrix[edge[1]][edge[0]] = weight
                adjacency_list[edge[1]].append((edge[0], weight))
            else:
                adjacency_matrix[edge[1]][edge[0]] = 1
                adjacency_list[edge[1]].append(edge[0])

    return adjacency_matrix, adjacency_list


def print_graph(adjacency_matrix, adjacency_list):
    print("Macierz sąsiedztwa:")
    print(adjacency_matrix)

    print("\nLista sąsiedztwa:")
    for key, values in adjacency_list.items():
        print(f"{key}: {list(values)}")


if __name__ == "__main__":
    adjacency_matrix, adjacency_list = create_graph()
    print_graph(adjacency_matrix, adjacency_list)
