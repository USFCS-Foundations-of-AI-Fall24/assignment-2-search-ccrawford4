import math
from queue import PriorityQueue

from Graph import Graph, Node, Edge
from mars_planner import mission_complete

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

    def  read_mars_graph(self, filename):
        g = Graph()
        location_to_node = {}
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip("\n")
                parts = line.split(":")
                source_location = parts[0].strip()
                if source_location not in location_to_node:
                    location_to_node[source_location] = Node(source_location)
                destination_strings = parts[1].strip().split(" ")
                for destination in destination_strings:
                    if destination not in location_to_node:
                        location_to_node[destination] = Node(destination)
                    edge = Edge(location_to_node[source_location], location_to_node[destination])
                    g.add_edge(edge)
        self.mars_graph = g


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    search_queue.put(start_state)
    closed_list = {}
    states = 0

    if use_closed_list:
        closed_list[start_state] = True
    while search_queue.qsize() > 0:
        next_state = search_queue.get()
        if goal_test(next_state):
            ptr = next_state
            while ptr is not None:
                ptr = ptr.prev_state
            return next_state, states
        else:
            src_node = Node(next_state.location)
            edges = next_state.mars_graph.get_edges(src_node)
            successors = []
            for edge in edges :
                new_state = map_state(
                    location=edge.dest.value,
                    mars_graph=next_state.mars_graph,
                    prev_state=next_state,
                    g=heuristic_fn(src_node.value),
                )
                successors.append(new_state)
            states += len(successors)
            if use_closed_list:
                successors = [item for item in successors
                              if item not in closed_list]
                for s in successors:
                    closed_list[s] = True
            for successor in successors :
                search_queue.put(successor)
    return None, states


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

def sld(location) :
    location = location.split(",")
    x1 = int(location[0])
    y1 = int(location[1])
    return math.sqrt(math.pow(x1 - 1, 2) + math.pow(y1 - 1, 2))

if __name__ == '__main__':
    start = map_state(location="8,8")     # Starting at the
    start.read_mars_graph('marsmap.txt')

    def mission_complete(state) :
        return state.is_goal()
    print("Number of states: ", a_star(start_state=start, heuristic_fn=sld, goal_test=mission_complete)[1])
