#!/usr/bin/python3

import unittest

from rover import RoverManager


class TestRovers(unittest.TestCase):
	def test_rovers_ok(self):
		data = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""
		rm = RoverManager()
		result = rm.instruct(data)
		expected = """1 3 N
5 1 E"""
		self.assertEqual(result, expected)	

	def test_large_plateau_ok(self):
		data = """10000 20000
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""
		rm = RoverManager()
		result = rm.instruct(data)
		expected = """1 3 N
5 1 E"""
		self.assertEqual(result, expected)	

	def test_rover_stops_at_top_edge_of_plateau(self):
		data = """5 5
0 0 N
MMMMMM"""
		rm = RoverManager()
		result = rm.instruct(data)
		expected = "0 5 N"
		self.assertEqual(result, expected)

	def test_rover_stops_at_bottom_edge_of_plateau(self):
		data = """5 5
0 5 S
MMMMMM"""
		rm = RoverManager()
		result = rm.instruct(data)
		expected = "0 0 S"
		self.assertEqual(result, expected)

	def test_rover_stops_before_crashing_with_another_rover(self):
		data = """5 5
0 0 N
MM
0 0 N
MM"""
		rm = RoverManager()
		result = rm.instruct(data)
		expected = """0 2 N
0 1 N"""
		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()
