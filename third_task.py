import networkx as nx

def finder(graph, str, visited):

    visited[str] = True
    print("visited: ---> ", visited, "\n")

    print(str, graph.adj[str])

    "Проход по графу"
    for node in graph.adj[str]:
        if not visited[node]:  # if not visited
            finder(graph, node, visited)

    return None

if __name__ == "__main__":
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHJKL")
    graph.add_edges_from([('A', 'B'),
						  ('B', 'C'),
						  ('C', 'D'),
						  ('F', 'G'),
						  ('G', 'H'),  #*тестовые строки
						  ('J', 'K'),  #*
						  ('K', 'L')]) #*

    visited = {node: False for node in graph.nodes()}
    num = 0

    for node in graph.adj:
        if not visited[node]:  # if not visited
            finder(graph, node, visited)
            num += 1
            print("-----")
    print(num)