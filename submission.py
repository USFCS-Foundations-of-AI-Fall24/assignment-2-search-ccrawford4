from atenna import run_antenna_solver
from mars_planner import run_mars_planner_algorithms
from routefinder import run_route_finder_algorithms

if __name__ == "__main__":
    print("-----------Antenna------------")
    run_antenna_solver()
    print("----------BFS, DFS, Depth-Limited DFS, and IDS before AND after problem decomposition--------")
    run_mars_planner_algorithms()
    print("---------A* and Uniform Cost Search--------------")
    run_route_finder_algorithms()