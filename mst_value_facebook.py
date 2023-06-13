import networkx as nx

# Create the graph from the dataset
G = nx.Graph()
with open("facebook_combined.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        node1 = data[0]
        node2 = data[1]
        G.add_edge(node1, node2)

# Find the minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Print the edges of the minimum spanning tree
for edge in mst.edges():
    print(edge)
