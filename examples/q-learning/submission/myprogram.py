import os
import json
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class Sender:
    """
    A Q-learning agent that sends messages to a Receiver
    """

    def __init__(self, num_sym: int, grid_rows: int, grid_cols: int, alpha_i: float, alpha_f: float, num_ep: int, epsilon: float, discount: float):
        """
        Initializes this agent with a state, set of possible actions, and a means of storing Q-values

        :param num_sym: The number of arbitrary symbols available for sending
        :type num_sym: int
        :param grid_rows: The number of rows in the grid
        :type grid_rows: int
        :param grid_cols: The number of columns in the grid
        :type grid_cols: int
        :param alpha_i: The initial learning rate
        :type alpha: float
        :param alpha_f: The final learning rate
        :type alpha: float
        :param num_ep: The total number of episodes
        :type num_ep: int
        :param epsilon: The epsilon in epsilon-greedy exploration
        :type epsilon: float
        :param discount: The discount factor
        :type discount: float
        """
        self.actions = range(num_sym)
        self.alpha = alpha_i
        self.alpha_i = alpha_i
        self.alpha_f = alpha_f
        self.num_ep = num_ep
        self.epsilon = epsilon
        self.discount = discount
        self.q_vals = [[[0.0 for i in range(num_sym)] for j in range(grid_cols)] for k in range(grid_rows)]

    def select_action(self, state):
        """
        This function is called every time the agent must act. It produces the action that the agent will take
        based on its current state

        :param state: the state the agent is acting from, in the form (x,y), which are the coordinates of the prize
        :type state: (int, int)
        :return: The symbol to be transmitted (must be an int < N)
        :rtype: int
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def update_q(self, old_state, action, reward):
        """
        This function is called after an action is resolved so that the agent can update its Q-values

        :param old_state: the state the agent was in when it acted, in the form (x,y), which are the coordinates
                          of the prize
        :type old_state: (int, int)
        :param action: the action that was taken
        :type action: int
        :param reward: the reward that was received
        :type reward: float
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""


class Receiver:
    """
    A Q-learning agent that receives a message from a Sender and then navigates a grid

    """

    def __init__(self, num_sym: int, grid_rows: int, grid_cols: int, alpha_i: float, alpha_f: float, num_ep: int, epsilon: float, discount: float):
        """
        Initializes this agent with a state, set of possible actions, and a means of storing Q-values

        :param num_sym: The number of arbitrary symbols available for sending
        :type num_sym: int
        :param grid_rows: The number of rows in the grid
        :type grid_rows: int
        :param grid_cols: The number of columns in the grid
        :type grid_cols: int
        :param alpha_i: The initial learning rate
        :type alpha: float
        :param alpha_f: The final learning rate
        :type alpha: float
        :param num_ep: The total number of episodes
        :type num_ep: int
        :param epsilon: The epsilon in epsilon-greedy exploration
        :type epsilon: float
        :param discount: The discount factor
        :type discount: float
        """
        self.actions = [0, 1, 2, 3]  # Note: these correspond to [up, down, left, right]
        self.alpha = alpha_i
        self.alpha_i = alpha_i
        self.alpha_f = alpha_f
        self.num_ep = num_ep
        self.epsilon = epsilon
        self.discount = discount
        self.q_vals = [[[[0.0 for a in range(4)] for i in range(num_sym)] for j in range(grid_cols)] for k in range(grid_rows)]

    def select_action(self, state):
        """
        This function is called every time the agent must act. It produces the action that the agent will take
        based on its current state
        :param state: the state the agent is acting from, in the form (m,x,y), where m is the message received
                      and (x,y) are the board coordinates
        :type state: (int, int, int)
        :return: The direction to move, where 0 is up, 1 is down, 2 is left, and 3 is right
        :rtype: int
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""

    def update_q(self, old_state, new_state, action, reward):
        """
        This function is called after an action is resolved so that the agent can update its Q-values

        :param old_state: the state the agent was in when it acted in the form (m,x,y), where m is the message received
                          and (x,y) are the board coordinates
        :type old_state: (int, int, int)
        :param new_state: the state the agent entered after it acted
        :type new_state: (int, int, int)
        :param action: the action that was taken
        :type action: int
        :param reward: the reward that was received
        :type reward: float
        """
        """Your code here"""
        raise NotImplementedError()
        """End of your code"""


def get_grid(grid_name: str):
    """
    This function produces one of the three grids defined in the assignment as a nested list

    :param grid_name: the name of the grid. Should be one of 'fourroom', 'maze', or 'empty'
    :type grid_name: str
    :return: The corresponding grid, where True indicates a wall and False a space
    :rtype: list[list[bool]]
    """
    grid = [[False for i in range(5)] for j in range(5)]  # default case is 'empty'
    if grid_name == 'fourroom':
        grid[0][2] = True
        grid[2][0] = True
        grid[2][1] = True
        grid[2][3] = True
        grid[2][4] = True
        grid[4][2] = True
    elif grid_name == 'maze':
        grid[1][1] = True
        grid[1][2] = True
        grid[1][3] = True
        grid[2][3] = True
        grid[3][1] = True
        grid[4][1] = True
        grid[4][2] = True
        grid[4][3] = True
        grid[4][4] = True
    return grid


def legal_move(posn_x: int, posn_y: int, move_id: int, grid: list[list[bool]]):
    """
    Produces the new position after a move starting from (posn_x,posn_y) if it is legal on the given grid (i.e. not
    out of bounds or into a wall)

    :param posn_x: The x position (column) from which the move originates
    :type posn_x: int
    :param posn_y: The y position (row) from which the move originates
    :type posn_y: int
    :param move_id: The direction to move, where 0 is up, 1 is down, 2 is left, and 3 is right
    :type move_id: int
    :param grid: The grid on which to move, where False indicates a space and True a wall
    :type grid: list[list[bool]]
    :return: The new (x,y) position if the move was legal, or the old position if it was not
    :rtype: (int, int)
    """
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    new_x = posn_x + moves[move_id][0]
    new_y = posn_y + moves[move_id][1]
    result = (new_x, new_y)
    if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
        result = (posn_x, posn_y)
    else:
        if grid[new_y][new_x]:
            result = (posn_x, posn_y)
    return result


def print_s_policy(grid, sender):
    num_rows = len(grid)
    num_cols = len(grid[0])

    out = []

    rstr = "|"
    for j in range(num_cols):
        rstr += "----"
    rstr = rstr[0:(len(rstr) - 1)]
    rstr += "|"
    out.append(rstr)

    for i in range(num_rows):
        rstr = "|"
        for j in range(num_cols):
            if not grid[i][j]:
                q_state = sender.q_vals[i][j]
                max_a = 0
                for a in range(len(q_state)):
                    if q_state[a] > q_state[max_a]:
                        max_a = a
                rstr += " " + str(max_a) + " |"
            else:
                rstr += "   |"
        rstr += "\n|"
        for j in range(num_cols):
            rstr += "----"
        rstr = rstr[0:(len(rstr)-1)]
        rstr += "|"
        out.append(rstr)
    return '\n'.join(out)


def print_r_policy(grid, receiver):
    num_rows = len(grid)
    num_cols = len(grid[0])
    move_labels = [u"\u2191", u"\u2193", u"\u2190", u"\u2192",]

    out = []
    for s in range(len(receiver.q_vals[0][0])):
        out.append("for signal " + str(s) + ":")
        rstr = "|"
        for j in range(num_cols):
            rstr += "----"
        rstr = rstr[0:(len(rstr) - 1)]
        rstr += "|"
        out.append(rstr)

        for i in range(num_rows):
            rstr = "|"
            for j in range(num_cols):
                if not grid[i][j]:
                    q_state = receiver.q_vals[i][j][s]
                    max_a = 0
                    for a in range(len(q_state)):
                        if q_state[a] > q_state[max_a]:
                            max_a = a
                    rstr += " " + move_labels[max_a] + " |"
                else:
                    rstr += "   |"
            rstr += "\n|"
            for j in range(num_cols):
                rstr += "----"
            rstr = rstr[0:(len(rstr)-1)]
            rstr += "|"
            out.append(rstr)
        return '\n'.join(out)


def run_episodes(sender: Sender, receiver: Receiver, grid: list[list[bool]], num_ep: int, delta: float):
    """
    Runs the reinforcement learning scenario for the specified number of episodes

    :param sender: The Sender agent
    :type sender: Sender
    :param receiver: The Receiver agent
    :type receiver: Receiver
    :param grid: The grid on which to move, where False indicates a space and True a wall
    :type grid: list[list[bool]]
    :param num_ep: The number of episodes
    :type num_ep: int
    :param delta: The chance of termination after every step of the receiver
    :type delta: float [0,1]
    :return: A list of the reward received by each agent at the end of every episode
    :rtype: list[float]
    """
    reward_vals = []

    # Episode loop
    for ep in range(num_ep):
        # Set receiver starting position
        receiver_x = 2
        receiver_y = 2

        # Choose prize position
        prize_x = np.random.randint(len(grid[0]))
        prize_y = np.random.randint(len(grid))
        while grid[prize_y][prize_x] or (prize_x == receiver_x and prize_y == receiver_y):
            prize_x = np.random.randint(len(grid[0]))
            prize_y = np.random.randint(len(grid))

        # Initialize new episode
        message = sender.select_action((prize_x, prize_y))
        reward = 0.0

        # Receiver loop
        terminate = False
        while not terminate:
            action = receiver.select_action((message, receiver_x, receiver_y))
            new_x,  new_y = legal_move(receiver_x,  receiver_y,  action,  grid)
            if new_x == prize_x and new_y == prize_y:
                reward = 1.0
                terminate = True
            elif np.random.random() < delta:
                terminate = True
            receiver.update_q((message, receiver_x, receiver_y),  (message, new_x, new_y),  action,  reward)
            receiver_x = new_x
            receiver_y = new_y

        # Finish up episode
        sender.update_q((prize_x, prize_y), message, reward)
        sender.alpha -= (sender.alpha_i - sender.alpha_f) / sender.num_ep
        receiver.alpha -= (receiver.alpha_i - receiver.alpha_f) / receiver.num_ep
        reward_vals.append(reward)

    return reward_vals


if __name__ == "__main__":
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('dinput', help='directory to input data')
    parser.add_argument('doutput', help='directory to output data')
    parser.add_argument('--dcheckpoint', help='directory to save checkpoint', default=os.getcwd())
    parser.add_argument('--num_learn_episodes', type=int, default=100000, help='how many episodes to train')
    parser.add_argument('--num_test_episodes', type=int, default=1000, help='how many episodes to test')
    parser.add_argument('--num_signals', type=int, default=4)
    parser.add_argument('--discount', type=float, default=0.95, help='discount factor')
    parser.add_argument('--epsilon', type=float, default=0.1)
    parser.add_argument('--alpha_init', type=float, default=0.9)
    parser.add_argument('--alpha_final', type=float, default=0.01)
    parser.add_argument('--grid_name', choices=('fourroom', 'maze', 'empty'), default='fourroom')
    args = parser.parse_args()

    np.random.seed(0)

    grid = get_grid(args.grid_name)
    delta = 1 - args.discount

    # Initialize agents
    sender = Sender(args.num_signals, len(grid), len(grid[0]), args.alpha_init, args.alpha_final, args.num_learn_episodes, args.epsilon, args.discount)
    receiver = Receiver(args.num_signals, len(grid), len(grid[0]), args.alpha_init, args.alpha_final, args.num_learn_episodes, args.epsilon, args.discount)

    # Learn
    learn_rewards = run_episodes(sender, receiver, grid, args.num_learn_episodes, delta)
    print("Sender policy:")
    sender_policy = print_s_policy(grid, sender)
    print(sender_policy)
    print()
    print()
    print("Receiver policy:")
    receiver_policy = print_r_policy(grid, receiver)
    print(receiver_policy)

    # Test
    sender.epsilon = 0.0
    sender.alpha = 0.0
    sender.alpha_i = 0.0
    sender.alpha_f = 0.0
    receiver.epsilon = 0.0
    receiver.alpha = 0.0
    receiver.alpha_i = 0.0
    receiver.alpha_f = 0.0
    test_rewards = run_episodes(sender, receiver, grid, args.num_test_episodes, delta)

    rtrain = np.average(learn_rewards)
    rtest = np.average(test_rewards)

    # Print results
    print(f"Average reward during learning: {rtrain}")
    print(f"Average reward during testing: {rtest}")

    with open(os.path.join(args.doutput, 'output.json'), 'wt') as f:
        json.dump(dict(
            sender_policy=sender_policy,
            receiver_policy=receiver_policy,
            rtrain=rtrain,
            rtest=rtest,
        ), f, indent=2)
