import networkx as nx

def shortest_path(G, origin, destination):
    try:
        return nx.dijkstra_path(G, origin, destination)
    except nx.NetworkXNoPath:
        return f"No path between {origin} and {destination}"
