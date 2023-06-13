import networkx as nx
import matplotlib.pyplot as plt

plt.ion()

G = nx.Graph()
with open("Dataset\\facebook_combined.txt", "r") as file:
    for line in file:
        data = line.strip().split(" ")
        node1 = data[0]
        node2 = data[1]
        G.add_edge(node1, node2)

        nx.draw(G, with_labels=True)
        plt.pause(0.0000000000000000000000000000000000000001)
        plt.show()
        # plt.show(block = True)