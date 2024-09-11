from collections import deque

## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    states = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()

        if goal_test(next_state[0]):
            print("Goal found")
            print("Total States: ", states)
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                # dont like this print statement
                # print(ptr)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            states += len(successors)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)


### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    search_queue = deque()
    closed_list = {}

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)

## add iterative deepening search here

# depth limited search at depth 1, then depth 2, then depth 3, etc.
# Pros: has linear memory
# Cons: have to do repeated work
# To search to a depth of n + 2(n-1) + 4(n-1) + 8(n-3)
# O(b^d) -> breadth to the depth *in a binary tree would be O(2^depth)

# Heuristic search
# tradeoff -> this is specific to each problem
# How to improve the search queue

# Greedy Search
# Will always take the shortest path (but that doesn't mean its the optimal route)

# A* search
# defineA* f to be g(n) + h(n), where g is the cost so far and h is the estimate to the goal

# f = g(s) + h(s)
# f = what is the cost to get to it + estimate for the quality of the solution from that state to the goal
#

# start at (8,8) -> the heuristic will just be h = (x2-x1)2 + (y2-y1)2
# heuristic = 0 in this case
# we are doing a straight line

# uniform cost search is just a special case of A*