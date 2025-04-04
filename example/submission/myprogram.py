#!/usr/bin/env python
import os
import string
import random
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def predict_next_char(prefix: str):
    """
    Your code here.
    """
    # the default implementation just predicts a random character each time
    top_guesses = [random.choice(all_chars) for _ in range(3)]
    return ''.join(top_guesses)


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    args = parser.parse_args()

    random.seed(0)

    all_chars = string.ascii_letters
    with open(os.path.join(args.dinput, 'input.txt')) as f:
        lines = f.readlines()

    print('Writing predictions')
    with open(os.path.join(args.doutput, 'output.txt'), 'wt') as f:
        for line in lines:
            completion = predict_next_char(line[:-1])  # remove trailing newline
            f.write(completion + '\n')
    print('Done!')
