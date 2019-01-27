def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
def find_isolated(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    return isolated

def add_vertex(graph, vertex)
    if vertex not in graph:
        graph_dict[vertex] = []


graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
print(generate_edges(graph))
print(find_isolated(graph))