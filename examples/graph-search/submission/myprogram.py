#!/usr/bin/env python
import os
import math
import json
import random
from collections import defaultdict
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def random_explore(graph, source, goal):
    visited = []
    frontier = [source]
    while frontier:
        node = random.choice(frontier)
        frontier.remove(node)
        visited.append(node)
        if node == goal:
            break
        else:
            for neighbour, cost in graph.neighbours[node]:
                frontier.append(neighbour)
    return visited


def break_ties(neighbors):
    return sorted(neighbors)


def heuristic(graph, s, t) -> float:
    slat, slong = graph.lat_long[s]
    tlat, tlong = graph.lat_long[t]
    dist = math.sqrt((slat - tlat)**2 + (slong - tlong)**2)
    return dist


def bfs(graph, source, goal):
    """
    Your code here.
    """
    return random_explore(graph, source, goal)


def dfs(graph, source, goal):
    """
    Your code here.
    """
    return random_explore(graph, source, goal)


def lowest_cost_first(graph, source, goal):
    """
    Your code here.
    """
    return random_explore(graph, source, goal)


def astar(graph, source, goal):
    """
    Your code here.
    """
    return random_explore(graph, source, goal)


class Graph:

    def __init__(self, nodes, edges):
        # mapping from node to neighbours
        self.lat_long = {place: (lat, long) for place, lat, long in nodes}
        self.neighbours = defaultdict(list)
        for s, t, c in edges:
            self.neighbours[s].append((t, c))


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
