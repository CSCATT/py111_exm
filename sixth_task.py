import networkx as nw

orders = [(9, 12), (12, 15), (15, 16), (15, 22)] # потому что 15-22 наслаивается на 15-16. Уберите заказ [, (15, 22)]

a = True

graph = nw.MultiDiGraph()
graph.add_nodes_from(range(0, 23))

for order in orders:
    for i in range(order[0], order[1]):
        graph.add_edge(i, i+1)

for d in graph.out_degree:
    if d[1] > 1:
        a = False
        break

print(a)