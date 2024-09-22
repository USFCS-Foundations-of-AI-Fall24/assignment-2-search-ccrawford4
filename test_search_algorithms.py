from unittest import TestCase
from mars_planner import *
from search_algorithms import *


class Test(TestCase):
    action_list = [move_to_sample, pick_up_tool, use_tool, drop_tool,
                   pick_up_sample, move_to_station, drop_sample,
                   move_to_battery, charge]

    def test_breadth_first_search(self):
        def g(s):
            return s.loc == "battery"
        s = RoverState()
        result = breadth_first_search(s, self.action_list, g)
        print(result)
        def g2(s):
            return s.loc == "sample" and s.sample_extracted == True
        s2 = RoverState()
        result = breadth_first_search(s2, self.action_list, g2)
        print(result)
        def g3(s) :
            return s.charged == True and s.sample_extracted == True
        s3 = RoverState()
        result = breadth_first_search(s3, self.action_list, g3)
        print(result)

    def test_depth_first_search(self):
        def g(s):
            return s.loc == "battery"
        s = RoverState()
        result = depth_first_search(s, self.action_list, g)
        print(result)
        def g2(s):
            return s.loc == "sample" and s.sample_extracted == True
        s2 = RoverState()
        result = depth_first_search(s2, self.action_list, g2)
        print(result)
        def g3(s) :
            return s.charged == True and s.sample_extracted == True
        s3 = RoverState()
        result = depth_first_search(s3, self.action_list, g3)
        print(result)