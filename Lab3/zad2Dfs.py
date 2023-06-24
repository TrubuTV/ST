def DFS(G):
    for u in G.vertices:
        u.p = -1
        u.visited = False
    time = 0

    for u in G.vertices:
        if not u.visited:
            DFS_Explore(u, time)


def DFS_Explore(u, time):
    time += 1
    u.time_1 = time
    u.visited = True

    for v in u.neighbors:
        if not v.visited:
            v.p = u
            DFS_Explore(v, time)

    time += 1
    u.time_2 = time
