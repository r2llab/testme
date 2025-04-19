#!/usr/bin/env python
import os
import sys
import copy
import json
import random
import inspect
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class CSP:

    def __init__(self, variables: dict, unary_constraints: dict, binary_constraints: dict):
        """
        - variables is a dictionary of variable name -> list of values in its domain
        - unary_constraints is a dictionary of variable name to functions
        - binary_constraints is a dictionary of a tuple of two variable names to functions

        Each constraint function takes the value(s) of the variable(s) and returns whether the value assignment meets the contraint.
        """
        self.variables = variables
        # enforce unary constraints
        for var, fconstraint in unary_constraints:
            self.variables[var] = [value for value in self.variables[var] if fconstraint(value)]
        # store binary constraints
        self.binary_constraints = {}
        print('Created CSP with constraints:')
        for (a, b), fcons in binary_constraints.items():
            self.binary_constraints[(a, b)] = fcons
            print(a, b, inspect.getsource(fcons).strip())


def ac3_one_step(csp: CSP, binary_constraint_satisfied: dict) -> dict:
    """
    Performs (in place) one round of AC3
    - binary_constraint_satisfied is a dictionary of tuple of variable names to whether this constraint has been satisfied
    """
    """Your code here"""
    raise NotImplementedError()
    """End of your code"""


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    parser.add_argument('--max_iter', default=30, type=int, help='max iterations to run')
    args = parser.parse_args()

    sys.path.append(os.path.join(args.dinput))
    import csp as P
    random.seed(0)

    csp = CSP(P.variables, P.unary, P.binary)
    binary_constraint_satisfied = {vars: False for vars in csp.binary_constraints}
    print('Round 0')
    print('Current domain:')
    print(csp.variables)

    rounds = []
    for round in range(args.max_iter):
        print(f'----- Round {round+1} -----')
        domain = copy.deepcopy(csp.variables)
        rounds.append(domain)
        ac3_one_step(csp, binary_constraint_satisfied)
        print('Current domain:')
        print(csp.variables)
        if all(binary_constraint_satisfied.values()):
            break

    with open(os.path.join(args.doutput, 'output.json'), 'wt') as f:
        json.dump(rounds[-1], f, indent=2)

    print('Done!')
