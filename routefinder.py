from queue import PriorityQueue

from Graph import Graph, Node, Edge


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    # Look at the depth
    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    # (x2-x1)2 + (y2-y1)
    sqt(a^ + b2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    g = Graph()
    with open (filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            parts = line.split(":")
            source = Node(parts[0].strip()) # Source node
            g.add_node(source)
            destination_strings = parts[1].strip().split(" ")
            for destination in destination_strings:
                destination_node = Node(destination)
                g.add_node(destination_node)
                edge = Edge(source, destination_node)
                g.add_edge(edge)

if __name__ == '__main__':
    read_mars_graph('marsmap.txt')
