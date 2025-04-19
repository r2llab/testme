import os
import bz2
import json
import tqdm
import typing as T
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class Layer:

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, dout):
        raise NotImplementedError()

    def update(self, learning_rate):
        pass

    def to_dict(self):
        return dict(name=self.__class__.__name__)

    @classmethod
    def from_dict(cls, d: dict):
        return cls()


class Sigmoid(Layer):

    def __init__(self):
        # storage for intermediate values
        self.z = None

    def forward(self, x):
        """
        Return the post activation output
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def backward(self, dz):
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""


class Linear(Layer):

    def __init__(self, dinp, dout, low=-1e-2, high=1e-2):
        self.dinp = dinp
        self.dout = dout
        self.W = np.random.uniform(low, high, size=(dinp, dout))
        self.b = np.random.uniform(low, high, size=(1, dout))

        # intermediate results
        self.x = self.a = self.z = None
        self.dW = self.db = None

    def to_dict(self):
        d = super().to_dict()
        d.update(dict(W=self.W.tolist(), b=self.b.tolist()))
        return d

    @classmethod
    def from_dict(cls, d: dict):
        W = np.array(d['W'])
        b = np.array(d['b'])
        dinp, dout = W.shape
        layer = cls(dinp, dout)
        layer.W = W
        layer.b = b
        return layer

    def forward(self, x: np.ndarray):
        """
        Compute the forward pass given input x of size self.dinp.
        Store intermediate results in self.a (before activation) and self.z (after activation).
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def backward(self, da: np.ndarray):
        """
        Compute the backward pass given gradient of objective funtion wrt self.a.
        Store intermediate results in self.dW and self.db.
        Return gradient with respect to input dx.
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def update(self, learning_rate: float):
        """
        Adjust the parameters given the learning rate and the previously computed gradients.
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""


class NeuralNet:

    def __init__(self, layers):
        self.layers = layers

    def save(self, dout):
        """
        Save necessary states to the output directory.
        """
        with bz2.open(os.path.join(dout, 'state.json.bz2'), 'wt') as f:
            json.dump(dict(
                layers=[layer.to_dict() for layer in self.layers],
            ), f)

    @classmethod
    def load(cls, dout):
        """
        Loads model from directory.
        """
        with bz2.open(os.path.join(dout, 'state.json.bz2'), 'rt') as f:
            d = json.load(f)
        L = {
            'Linear': Linear,
            'Sigmoid': Sigmoid,
        }
        layers = [L[x['name']].from_dict(x) for x in d['layers']]
        return cls(layers)

    def compute_error(self, estimate: float, target: float) -> T.Tuple[float, float]:
        """
        Compute the squared error and return a tuple of two floats:
            (the error, its gradient wrt the estimate).
        Your code here.
        """
        error = (estimate - target)
        return error ** 2, 2 * error
        """End of your code"""

    def train(self, data: list, num_steps: int, learning_rate: float):
        """
        Train from a list of examples
        """
        errors = []
        for step in (bar := tqdm.trange(num_steps, desc='Training..')):
            ex = np.random.choice(data)
            x = np.array([ex['x']])  # insert a fake batch dimension for easier matrix multiplies
            out = x
            for layer in self.layers:
                out = layer.forward(out)
            error, derror = self.compute_error(out, ex['y'])
            errors.append(error.item())
            bar.set_description(f'Training (err={error})')

            for layer in reversed(self.layers):
                derror = layer.backward(derror)
            for layer in self.layers:
                layer.update(learning_rate)
        return errors

    def predict(self, data: list) -> list:
        """
        Predict target for a list of examples.
        Your code here.
        """
        preds = []
        for ex in data:
            x = np.array([ex['x']])  # insert a fake batch dimension for easier matrix multiplies
            out = x
            for layer in self.layers:
                out = layer.forward(out)
            preds.append(out.item())
        return preds
        """End of your code"""


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    parser.add_argument('--dcheckpoint', help='directory to save checkpoint', default=os.getcwd())
    parser.add_argument('--train', action='store_true', help='train the model')
    parser.add_argument('--num_steps', type=int, default=1000, help='how many steps to train')
    parser.add_argument('--learning_rate', type=float, default=1e-3, help='learning rate')
    args = parser.parse_args()

    np.random.seed(0)

    splits = ['test']
    if args.train:
        splits.extend(['train', 'val'])
    data = {}
    for split in splits:
        fname = os.path.join(args.dinput, f'{split}.json.bz2')
        if os.path.isfile(fname):
            print(f'Loading {fname}')
            with bz2.open(fname, 'rt') as f:
                data[split] = json.load(f)

    if args.train:
        layers = [
            Linear(2, 5),
            Sigmoid(),
            Linear(5, 1),
        ]
        nn = NeuralNet(layers)
        errors = nn.train(data['train'], num_steps=args.num_steps, learning_rate=args.learning_rate)
        nn.save(args.dcheckpoint)
        with bz2.open(os.path.join(args.doutput, 'train_log.json'), 'wt') as f:
            json.dump(errors, f, indent=2)

    nb = NeuralNet.load(args.dcheckpoint)

    if args.train:
        pred = nb.predict(data['val'])
        mse = sum((p - ex['y'])**2 for ex, p in zip(data['val'], pred)) / len(data['val'])
        print(f'Validation MSE: {mse}')

    pred = nb.predict(data['test'])
    print('Making predictions on test')
    with bz2.open(os.path.join(args.doutput, 'output.json.bz2'), 'wt') as f:
        json.dump(pred, f, indent=2)
