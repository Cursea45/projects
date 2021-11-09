import matplotlib.pyplot as plt
import networkx as nx

G1=nx.DiGraph()
G1.add_node(0)
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)
G1.add_edge(0,1,weight=5.0)
G1.add_edge(0,2,weight=3.0)
G1.add_edge(0,4,weight=2.0)
G1.add_edge(1,2,weight=2.0)
G1.add_edge(1,3,weight=6.0)
G1.add_edge(2,1,weight=1.0)
G1.add_edge(2,3,weight=2.0)
G1.add_edge(4,1,weight=6.0)
G1.add_edge(4,2,weight=10.0)
G1.add_edge(4,3,weight=4.0)
elarge = [(u, v) for (u, v, d) in G1.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G1.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G1)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G1, pos, node_size=700)

# edges
nx.draw_networkx_edges(G1, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G1, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# labels
nx.draw_networkx_labels(G1, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()




sp1 = nx.dijkstra_path(G1,source = 4, target = 1)
sp2 = nx.dijkstra_path(G1,source = 4, target = 2)
sp3 = nx.dijkstra_path(G1,source = 4, target = 3)
print("EN KISA YOLLAR:\n4ten 1'e",sp1,"\n4ten 2'ye:",sp2,"\n4'ten 3 e:",sp3)

G1.remove_node(3)
elarge = [(u, v) for (u, v, d) in G1.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G1.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G1)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G1, pos, node_size=700)

# edges
nx.draw_networkx_edges(G1, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G1, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# labels
nx.draw_networkx_labels(G1, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
sp1 = nx.dijkstra_path(G1,source = 4, target = 1)
sp2 = nx.dijkstra_path(G1,source = 4, target = 2)

print("EN KISA YOLLAR:\n4ten 1'e",sp1,"\n4ten 2'ye:",sp2)