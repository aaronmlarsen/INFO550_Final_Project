from search import *


class Counter(dict):
    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)


class MCTS:
    def __init__(self, c=1):
        self.Q = Counter()
        self.N = Counter()
        self.children = {}
        self.c = c

    def choose_action(self, board):
        if board not in self.children:
            return board.random_child()
        else:
            legal_actions = board.get_legal_actions()
            action_values = np.zeros(len(legal_actions))
            for i, a in enumerate(legal_actions):
                action_values[i] = self.Q[board] / self.N[board]
            ind = np.argmax(action_values)
            return legal_actions[ind]

    def UCTsearch(self, board):
        path = []
        while True:
            path.append(board)
            if (board not in self.children.keys()) or (self.children[board] is None):
                return path
            else:
                not_explored = [child for child in self.children[board] if child not in self.children.keys()]
                if len(not_explored) > 0:
                    next_board = not_explored.pop()
                    path.append(next_board)
                    return path
                else:
                    next_move = self.select_move(board)
                    new_board = board.make_action(board.state, next_move, board.board_size)
                    board = new_board

    def select_move(self, board):
        legal_actions = board.get_legal_actions()
        UCT_values = np.zeros(len(legal_actions))
        for i, a in enumerate(legal_actions):
            UCT_values[i] = self.Q[board] + \
                            self.c * np.sqrt(np.log(self.N[board]) / self.N[board])
        ind = np.argmax(UCT_values)
        return legal_actions[ind]

    def rollout(self, board):
        path = self.UCTsearch(board)
        leaf = path[-1]
        self.expand(leaf)
        reward = self.simulate(leaf)
        self.backprop(path, reward)

    def expand(self, board):
        if board not in self.children.keys():
            self.children[board] = board.get_children()

    def backprop(self, path, reward):
        for board in path:
            self.N[board] += 1
            self.Q[board] += (reward - self.Q[board]) / self.N[board]
            reward = 1 - reward

    def simulate(self, board):
        while True:
            if board.terminal:
                reward = board.reward
                return reward
            else:
                board = board.random_child()


class Board:
    def __init__(self, state=None, turn=None, board_size=3):
        self.board_size = board_size
        if state is None:
            self.state = np.zeros((board_size, board_size))
            self.real_state = np.zeros((board_size, board_size))
        else:
            self.state = state
        if turn is None:
            self.turn = 0  # Starts with player 1 turn
        else:
            self.turn = turn
        self.is_terminal()  # Set terminal and winner
        if self.terminal:
            self.get_reward()

    def get_legal_actions(self):
        return [tuple(i) for i in np.argwhere(self.state == 0)]

    def make_action(self, old_state, a, board_size):
        state = np.copy(old_state)
        if self.turn == 0:
            state[a] = 1
        if self.turn == 1:
            state[a] = -1
        turn = (self.turn + 1) % 2
        return Board(state, turn, board_size)

    def get_children(self):
        if self.is_terminal():
            return []  # No duplciates
        else:
            next_states = [self.make_action(self.state, a, self.board_size) for a in self.get_legal_actions()]

    def random_child(self):
        if self.is_terminal():
            return None  # No child
        else:
            index = np.random.choice(len(self.get_legal_actions()))
            action = self.get_legal_actions()[index]
            random_child = self.make_action(self.state, action, self.board_size)
            return random_child

    def is_terminal(self):
        terminal = False
        winner = None

        cols = np.sum(self.state, 0)
        rows = np.sum(self.state, 1)
        diag1 = np.trace(self.state)
        diag2 = np.trace(np.fliplr(self.state))
        board_size = self.board_size
        if (board_size in cols) or (board_size in rows) or (diag1 == board_size) or (diag2 == board_size):
            terminal = True
            winner = 0  # Player 1
        elif (-board_size in cols) or (-board_size in rows) or (diag1 == -board_size) or (diag2 == -board_size):
            terminal = True
            winner = 1  # Player 2
        elif len(np.argwhere(self.state == 0)) == 0:
            terminal = True
            winner = 2  # Draw

        self.terminal = terminal
        self.winner = winner

    def get_reward(self):
        if self.winner == 2:
            self.reward = 0.5
        elif self.winner == 1 and self.turn == 1:
            self.reward = 1
        elif self.winner == 0 and self.turn == 0:
            self.reward = 1
        else:
            self.reward = 0


def show_tic_tac_toe(board):
    b = (-1 * np.ones_like(board)).astype('<U1')

    ind1 = [tuple(i) for i in np.argwhere(board == 1)]
    ind2 = [tuple(i) for i in np.argwhere(board == -1)]
    ind3 = [tuple(i) for i in np.argwhere(b == b[0, 0])]

    for i in ind3:
        b[i] = ""
    for i in ind1:
        b[i] = "X"
    for i in ind2:
        b[i] = "O"

    for ind, i in enumerate(b):
        string = " "
        for ind2, j in enumerate(i):
            if j == "":
                string += " "
            else:
                string += j
            if ind2 != (len(board) - 1):
                string += " | "
            else:
                string += " "
        if ind != (len(board) - 1):
            print("\u0332".join(string + " "))
        else:
            print(string)
