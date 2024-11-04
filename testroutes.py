import unittest
from data_processing import load_and_clean_data
from algorithms import shortest_path
import networkx as nx

class TestRouteSearch(unittest.TestCase):
    def setUp(self):
        self.G = nx.Graph()
        self.G.add_edge('A', 'B', weight=10)
        self.G.add_edge('B', 'C', weight=15)

    def test_shortest_path(self):
        result = shortest_path(self.G, 'A', 'C')
        self.assertEqual(result, ['A', 'B', 'C'])

if __name__ == '__main__':
    unittest.main()
