# Find the maximum number of edges you can remove from a tree such that each resulting
# connected component contains an even number of vertices.


def traverse(graph, vertex, exclude):
    numVertices = 0
    for e in graph:
        if e not in exclude and (e[0] == vertex or e[1] == vertex):
            exclude.append(e)
            numVertices = traverse(graph, e[1] if e[0] == vertex else e[0], exclude)

    return numVertices + 1


# Divide the tree into two (disjoint) connected components by removing an edge
def divide(graph, edge):
    n1 = 0  # Size of the first component
    n2 = 0  # Size of the second component
    for e in graph:
        if e != edge:
            if e[0] == edge[0] or e[1] == edge[0]:
                n1 = traverse(graph, e[1] if e[0] == edge[0] else e[0], [edge])
            elif e[0] == edge[1] or e[1] == edge[1]:
                n2 = traverse(graph, e[1] if e[0] == edge[1] else e[0], [edge])

            if n1 > 0 and n2 > 0:
                return n1, n2

    return 1, 1


if __name__ == '__main__':
    # Intuition: An edge remains iff one of the resulting components
    # after removing that edge has an odd number of vertices.
    numVertices, numEdges = (int(x) for x in raw_input().strip().split())

    graph = []
    for i in range(numEdges):
        edge = tuple(int(x) for x in raw_input().strip().split())
        graph.append(edge)

    n = 0
    for edge in graph:
        n1, n2 = divide(graph, edge)
        if n1 % 2 == 0 and n2 % 2 == 0:
            n += 1

    print n
