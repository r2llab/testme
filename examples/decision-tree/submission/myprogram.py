#!/usr/bin/env python
import os
import json
import math
import random
from queue import PriorityQueue
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class Node:

    def __init__(self, parent, feature: str, value: bool, data: list, info_gain: float = 0):
        self.parent = parent  # parent node
        self.feature = feature  # which feature this node splits on
        self.value = value  # feature value of this node
        self.data = data  # which subset of data this node has
        self.info_gain = info_gain  # information gain for the split that created this node
        self.children = {}  # map from feature value to child node

    def __gt__(self, other):
        return repr(self) > repr(other)

    def __repr__(self):
        num_yes = sum(ex['y'] for ex in self.data)
        num_no = len(self.data) - num_yes
        return f'{self.parent} --> {self.feature}={self.value} (y:{num_yes} n:{num_no} ' + 'IG:{:.3f})'.format(self.info_gain)

    def to_dict(self):
        me = dict(feature=self.feature, value=self.value, info_gain=self.info_gain, children={k: n.to_dict() for k, n in self.children.items()})
        return me

    def is_leaf(self) -> bool:
        """Returns whether this node is a leaf node."""
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def get_point_estimate(self):
        assert self.is_leaf(), f'leaf node has more than 1 class assignment: {self.data}'
        return self.data[0]['y']


class DecisionTree:

    def __init__(self, tree: Node = None):
        self.root = tree

    @classmethod
    def calculate_info(cls, data: list) -> float:
        """Returns the total information of this dataset"""
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def train(self, data):
        """Creates the decision tree by splitting using the data."""
        self.root = Node(parent=None, feature='root', value=True, data=data)
        queue = PriorityQueue()
        queue.put((1, [self.root]))

        features = data[0]['x'].keys()

        while not queue.empty():
            # get a split from the pqueue
            priority, nodes = queue.get()
            parent = nodes[0].parent

            if parent:
                if parent.children:
                    # this parent has already been split, so ignore this split
                    continue
                else:
                    # actually insert split into tree
                    for n in nodes:
                        print(f'inserting {n}')
                        parent.children[f'{n.feature}={n.value}'] = n

            for node in nodes:
                if node.is_leaf():
                    continue

                # insert possible next splits into the pqueue
                initial_info = self.calculate_info(node.data)
                for f in features:
                    yes = [ex for ex in node.data if ex['x'][f]]
                    no = [ex for ex in node.data if not ex['x'][f]]

                    if (not yes) or (not no):
                        # zero gain
                        continue

                    split_info = len(yes) / len(node.data) * self.calculate_info(yes) + len(no) / len(node.data) * self.calculate_info(no)
                    info_gain = initial_info - split_info

                    priority = -info_gain  # negate because queue is lowest first by default
                    """Add next possible nodes into the queue"""
                    """Your code here"""
                    raise NotImplementedError()
                    """End of your code"""

    def predict(self, x) -> bool:
        """Make a prediction for the given features"""
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    args = parser.parse_args()

    random.seed(0)

    with open(os.path.join(args.dinput, 'data.json')) as f:
        data = json.load(f)
    with open(os.path.join(args.dinput, 'query.json')) as f:
        query = json.load(f)

    print('building decision tree')
    d = DecisionTree()
    d.train(data)

    with open(os.path.join(args.doutput, 'tree.json'), 'wt') as f:
        json.dump(d.root.to_dict(), f, indent=2)

    ys = []
    for ex in query:
        ys.append(d.predict(ex['x']))

    with open(os.path.join(args.doutput, 'pred.json'), 'wt') as f:
        json.dump(ys, f, indent=2)

    print('Done!')
