from unittest import TestCase
from mars_planner import *

class TestRoverState(TestCase):
    def test_move_to_sample(self):
        s = RoverState(loc="battery")
        s = move_to_sample(s)
        self.assertEqual(s.loc, "sample")

    def test_eq(self):
        s = RoverState(loc="battery")
        s2 = RoverState(loc="battery")
        self.assertEqual(s,s2)
        s3 = RoverState(loc="station")
        self.assertNotEqual(s, s3)

    def test_successors(self):
        action_list = [move_to_sample, pick_up_tool, use_tool, drop_tool,
                       pick_up_sample, move_to_station, drop_sample,
                       move_to_battery, charge]
        s=RoverState()
        slist = s.successors(action_list)
        self.assertEqual(len(slist), 2)

    def test_move_to_station(self):
        s = RoverState(loc="battery")
        s = move_to_station(s)
        self.assertEqual(s.loc, "station")

    def test_move_to_battery(self):
        s = RoverState(loc="sample")
        s = move_to_battery(s)
        self.assertEqual(s.loc, "battery")

    def test_pick_up_tool(self):
        s = RoverState()
        s = pick_up_tool(s)
        self.assertFalse(s.holding_tool)
        s = RoverState("sample")
        s = pick_up_tool(s)
        self.assertTrue(s.holding_tool)

    def test_use_tool(self):
        s = RoverState(holding_tool=False)
        s = use_tool(s)
        self.assertFalse(s.sample_extracted)

        s = RoverState("sample", holding_tool=True)
        s = use_tool(s)
        self.assertTrue(s.sample_extracted)

    def test_drop_tool(self):
        s = RoverState(holding_tool=False)
        s = drop_tool(s)
        self.assertFalse(s.holding_tool)

        s = RoverState(holding_tool=True)
        s = drop_tool(s)
        self.assertFalse(s.holding_tool)

    def test_pick_up_sample(self):
        s = RoverState(holding_tool=True, holding_sample=False)
        s = pick_up_sample(s)
        self.assertFalse(s.holding_sample)

        s = RoverState("sample", holding_tool=True, sample_extracted=True)
        s = pick_up_sample(s)
        self.assertTrue(s.holding_sample)

    def test_drop_sample(self):
        s = RoverState(holding_sample=False)
        s = drop_sample(s)
        self.assertFalse(s.holding_sample)

        s = RoverState(holding_sample=True, loc="station", sample_extracted=True)
        s = drop_sample(s)
        self.assertFalse(s.holding_sample)

    def test_charge(self):
        s = RoverState(sample_extracted=False, loc="sample")
        s = charge(s)
        self.assertFalse(s.charged)

        s = RoverState(sample_extracted=True, loc="sample")
        s = charge(s)
        self.assertTrue(s.charged)




