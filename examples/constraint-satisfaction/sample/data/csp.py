variables = dict(
    W1a=['ant', 'big', 'bus', 'car', 'has'],
    W1d=['book', 'buys', 'hold', 'lane', 'year'],
    W2d=['ginger', 'search', 'syntax', 'symbol'],
    W3a=['book', 'buys', 'hold', 'lane', 'year'],
    W4a=['ant', 'big', 'bus', 'car', 'has'],
)
unary = dict(
)
binary = {
    ('W2d', 'W3a'): lambda x, y: x[2] == y[2],
    ('W3a', 'W2d'): lambda x, y: x[2] == y[2],
    ('W1a', 'W2d'): lambda x, y: x[2] == y[0],
    ('W2d', 'W1a'): lambda x, y: x[0] == y[2],
    ('W1a', 'W1d'): lambda x, y: x[0] == y[0],
    ('W1d', 'W1a'): lambda x, y: x[0] == y[0],
    ('W3a', 'W1d'): lambda x, y: x[0] == y[2],
    ('W1d', 'W3a'): lambda x, y: x[2] == y[0],
    ('W2d', 'W4a'): lambda x, y: x[4] == y[0],
    ('W4a', 'W2d'): lambda x, y: x[0] == y[4],
}