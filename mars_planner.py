## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search, iterative_deepening_search


class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, charged=False, holding_tool=False):
        self.loc = loc
        self.sample_extracted=sample_extracted
        self.holding_sample = holding_sample
        self.charged=charged
        self.holding_tool=holding_tool
        self.prev = None

    def __eq__(self, other):
       return (
            self.loc == other.loc and
            self.sample_extracted == other.sample_extracted and
            self.holding_sample == other.holding_sample and
            self.charged == other.charged and
            self.holding_tool == other.holding_tool
       )


    def __repr__(self):
        return (
                f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}" +
                f"Holding Tool?: {self.holding_tool}"
        )

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.
def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev=state
    return r2

def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2

# add tool functions here
def pick_up_tool(state) :
    r2 = deepcopy(state)
    if sample_goal(state) :
        r2.holding_tool = True
    r2.prev = state
    return r2

def use_tool(state) :
    r2 = deepcopy(state)
    if sample_goal(state) and holding_tool_goal(state):
        r2.sample_extracted = True
    r2.prev = state
    return r2

def drop_tool(state) :
    r2 = deepcopy(state)
    if holding_tool_goal(state) :
        r2.holding_tool = False
    r2.prev = state
    return r2

def pick_up_sample(state) :
    r2 = deepcopy(state)
    if sample_extract_goal(state) and sample_goal(state) :
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if sample_extract_goal(state) and station_goal(state) :
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.charged = True
    r2.prev = state
    return r2

action_list = [move_to_sample, pick_up_tool, use_tool, drop_tool, pick_up_sample, move_to_station, drop_sample,
               move_to_battery, charge]

def battery_goal(state) :
    return state.loc == "battery"

def sample_goal(state) :
    return state.loc == "sample"

def station_goal(state) :
    return state.loc == "station"

# Other goal functions
def sample_extract_goal(state) :
    return state.sample_extracted

def charged_goal(state) :
    return state.charged

def holding_tool_goal(state) :
    return state.holding_tool

def mission_complete(state) :
    return battery_goal(state) and charged_goal(state) and sample_extract_goal(state)

if __name__=="__main__" :
    print("---------Before problem decomposition-----------")
    s = RoverState()
    print("Total States Using BFS: ", breadth_first_search(s, action_list, mission_complete))

    s = RoverState()
    depth_first_search(s, action_list, mission_complete, limit=9)

    s = RoverState()
    iterative_deepening_search(s, action_list, mission_complete)

    print("---------After problem decomposition------------")

    # Modify your search code so that it instead solves three subproblems: moveToSample, removeSample, and returnToCharger.
    s = RoverState()

    bfs_total_states = 0
    # First move to the sample
    action_list = [move_to_sample]
    bfs_total_states += breadth_first_search(s, action_list, sample_goal)


    # Second extract the sample
    # should be at the sample
    action_list = [pick_up_tool, use_tool, drop_tool, pick_up_sample]
    bfs_total_states += breadth_first_search(s, action_list, sample_extract_goal)

    # Return to charger
    action_list = [move_to_station, drop_sample, move_to_battery, charge]
    bfs_total_states += breadth_first_search(s, action_list, mission_complete)

    print("Total BFS States: ", bfs_total_states)