import os
import bz2
import json
import tqdm
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class KMeans:

    def __init__(self, num_clusters: int, num_features: int):
        # Hint: you must change this during training
        self.centroids = np.zeros((num_clusters, num_features))

    def save(self, dout):
        """
        Save necessary states to the output directory.
        """
        with bz2.open(os.path.join(dout, 'state.json.bz2'), 'wt') as f:
            json.dump(dict(
                centroids=self.centroids.tolist(),
            ), f)

    @classmethod
    def load(cls, dout):
        """
        Loads model from directory.
        """
        with bz2.open(os.path.join(dout, 'state.json.bz2'), 'rt') as f:
            d = json.load(f)
        centroids = np.array(d['centroids'])
        kmeans = cls(*centroids.shape)
        kmeans.centroids = centroids
        return kmeans

    def train(self, data: list, num_steps: int):
        """
        Train from a list of examples
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def predict(self, data: list) -> list:
        """
        Predict target for a list of examples.
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    parser.add_argument('--dcheckpoint', help='directory to save checkpoint', default=os.getcwd())
    parser.add_argument('--train', action='store_true', help='train the model')
    parser.add_argument('--num_steps', type=int, default=10, help='how many steps to train')
    parser.add_argument('--num_clusters', type=int, default=5, help='how many clusters')
    parser.add_argument('--num_features', type=int, default=5, help='how many features')
    args = parser.parse_args()

    np.random.seed(0)

    data = {}
    for split in ['train', 'test']:
        fname = os.path.join(args.dinput, f'{split}.json.bz2')
        if os.path.isfile(fname):
            print(f'Loading {fname}')
            with bz2.open(fname, 'rt') as f:
                data[split] = json.load(f)

    if args.train:
        kmeans = KMeans(num_clusters=args.num_clusters, num_features=args.num_features)
        kmeans.train(data['train'], num_steps=args.num_steps)
        kmeans.save(args.dcheckpoint)

    nb = KMeans.load(args.dcheckpoint)
    pred = nb.predict(data['test'])
    print('Making predictions on test')
    with bz2.open(os.path.join(args.doutput, 'output.json.bz2'), 'wt') as f:
        json.dump(pred, f, indent=2)
