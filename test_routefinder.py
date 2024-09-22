from unittest import TestCase
from routefinder import *

class Testmap_state(TestCase):
    def test_is_lt (self) :
        s1 = map_state(g = 1,h=1)
        s2 = map_state(g=2,h=2)
        print(s1 < s2)
        self.assertLessEqual(s1,s2)

    def test_sld(self) :
        s1 = map_state(location="3,2", g = 1,h=1)
        val = sld(s1.location)
        self.assertLessEqual(val, 14)

        s1.location = "8,9"
        self.assertEquals(sld(s1.location), 10.63014581273465)

    def test_read_mars_graph(self):
        test_state = map_state()
        test_state.read_mars_graph("test_marsmap.txt")

        expected_graph = Graph()
        node1 = Node("1,1")
        node2 = Node("1,2")
        node3 = Node("3,4")
        node4 = Node("3,2")
        node5 = Node("2,1")
        node6 = Node("3,1")
        expected_graph.add_edge(Edge(node1, node2))
        expected_graph.add_edge(Edge(node1, node3))
        expected_graph.add_edge(Edge(node4, node5))
        expected_graph.add_edge(Edge(node4, node6))

        self.assertEqual(test_state.mars_graph.g, expected_graph.g)

    def test_astar(self):
        test_state = map_state(location="8,8")
        test_state.read_mars_graph("marsmap.txt")

        def complete(state) :
            return state.location == "1,1"

        result = a_star(test_state, sld, complete)
        self.assertEqual(result[1], 61)

        test_state.location = "4,4"
        result = a_star(test_state, sld, complete)
        self.assertEqual(result[1], 41)


