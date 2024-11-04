import networkx as nx
import pandas as pd

def load_data(file_path):
    
    df = pd.read_csv(file_path)
    return df

def create_graph(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['origin'], row['destination'], weight=row['distance'])
    return G

def find_shortest_path(G, origin, destination):
    return nx.dijkstra_path(G, origin, destination)

if __name__ == "__main__":
    data_path = 'routes.csv'
    df = load_data(data_path)
    G = create_graph(df)
    origin, destination = input("Enter origin and destination: ").split()
    print(find_shortest_path(G, origin, destination))
