import networkx as nx
import matplotlib.pyplot as plt

plt.ion()

G = nx.Graph()
with open("temp_dataset.txt", "r") as file:
    for line in file:
        data = line.strip().split(" ")
        node1 = data[0]
        node2 = data[1]
        G.add_edge(node1, node2)
        nx.draw(G, with_labels=True)
        # plt.pause(0.1)
        plt.show(block=True)
        # plt.show()