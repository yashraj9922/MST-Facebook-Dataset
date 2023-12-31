import networkx as nx
import matplotlib.pyplot as plt

# Create the graph from the dataset
G = nx.Graph()
with open("Dataset\\temp_dataset.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        node1 = data[0]
        node2 = data[1]
        G.add_edge(node1, node2)

# Find the minimum spanning tree edges
mst_edges = nx.minimum_spanning_edges(G, algorithm='prim', data=False)

# Create a new graph with only the MST edges
mst = nx.Graph()
mst.add_edges_from(mst_edges)

# Visualize the MST edges
nx.draw(mst, with_labels=True)
plt.show(block=True)
