#!/usr/bin/env python
import os
import json
import random
import heapq
import geopy.distance
from collections import defaultdict, deque
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def break_ties(neighbors):
    return sorted(neighbors)


def heuristic(graph, s, t) -> float:
    slat, slong = graph.lat_long[s]
    tlat, tlong = graph.lat_long[t]
    d = geopy.distance.geodesic((slong, slat), (tlong, tlat)).km
    return d


def bfs(graph, source, goal):
    """Your code here"""
    raise NotImplementedError()
    """End of your code"""


def dfs(graph, source, goal):
    """Your code here"""
    raise NotImplementedError()
    """End of your code"""


def lowest_cost_first(graph, source, goal):
    """Your code here"""
    raise NotImplementedError()
    """End of your code"""


def astar(graph, source, goal):
    """Your code here"""
    raise NotImplementedError()
    """End of your code"""


class Graph:

    def __init__(self, nodes, edges):
        # mapping from node to neighbours
        self.lat_long = {place: (lat, long) for place, lat, long in nodes}
        self.neighbours = defaultdict(list)
        for s, t, c in edges:
            self.neighbours[s].append((t, c))
            self.neighbours[t].append((s, c))


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    args = parser.parse_args()

    random.seed(0)

    with open(os.path.join(args.dinput, 'nodes.json')) as f:
        nodes = json.load(f)
    with open(os.path.join(args.dinput, 'edges.json')) as f:
        edges = json.load(f)
    graph = Graph(nodes, edges)

    with open(os.path.join(args.dinput, 'query.json')) as f:
        source, target = json.load(f)

    tests = [bfs, dfs, lowest_cost_first, astar]
    for ftest in tests:
        print(f'Running {ftest.__name__} from {source} to {target}')
        order = ftest(graph, source, target)
        with open(os.path.join(args.doutput, f'{ftest.__name__}.json'), 'wt') as f:
            json.dump(order, f)

    print('Done!')
