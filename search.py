import numpy as np


def minimax(board, max_depth):
    def minimax_decision(board):
        possible_actions = board.get_legal_actions()  # Get legal moves
        values = np.zeros(len(possible_actions))  # Store each max value
        depth = 0
        for ind, action in enumerate(possible_actions):
            next_board = board.make_action(board.state, action, board.board_size)
            v = min_value(next_board, depth)
            values[ind] = v
        max_action = np.argmax(values)  # action with highest value
        best_action = possible_actions[max_action]  # best action
        return best_action

    def max_value(board, depth):
        # Check if win, lose, or max depth reached
        if board.terminal or depth == max_depth:
            return board.get_reward()

        possible_actions = board.get_legal_actions()  # Get possible actions
        values = np.zeros(len(possible_actions))  # Keep track of values corresp to actions
        for ind, action in enumerate(possible_actions):
            next_board = board.make_action(board.state, action, board.board_size)
            # Change player index
            if board.turn == 0:  # If pacman/player
                new_depth = depth + 1  # Increase depth since each player has moved
                val = max_value(next_board, new_depth)
            else:
                val = min_value(next_board, depth)
            values[ind] = val
        return np.max(values)

    def min_value(board, depth):
        # Check if win, lose, or max depth reached
        if board.terminal or depth == max_depth:
            return board.get_reward()

        possible_actions = board.get_legal_actions()  # Get possible actions
        values = np.zeros(len(possible_actions))  # Keep track of values corresp to actions
        for ind, action in enumerate(possible_actions):
            next_board = board.make_action(board.state, action, board.board_size)
            # Change player index
            if board.turn == 0:  # If pacman/player
                new_depth = depth + 1  # Increase depth since each player has moved
                val = max_value(next_board, new_depth)
            else:
                val = min_value(next_board, depth)
            values[ind] = val
        return np.min(values)

    return minimax_decision(board)


def expectimax(board, max_depth):
    def expectimax_decision(board):
        possible_actions = board.get_legal_actions()  # Get legal moves
        values = np.zeros(len(possible_actions))  # Store each max value
        depth = 0
        for ind, action in enumerate(possible_actions):
            next_board = board.make_action(board.state, action, board.board_size)
            v = exp_value(next_board, depth)
            values[ind] = v
        max_action = np.argmax(values)  # action with highest value
        best_action = possible_actions[max_action]  # best action
        return best_action

    def max_value(board, depth):
        # Check if win, lose, or max depth reached
        if board.terminal or depth == max_depth:
            return board.get_reward()

        possible_actions = board.get_legal_actions()  # Get possible actions
        values = np.zeros(len(possible_actions))  # Keep track of values corresp to actions
        for ind, action in enumerate(possible_actions):
            next_board = board.make_action(board.state, action, board.board_size)
            # Change player index
            if board.turn == 0:  # If pacman/player
                new_depth = depth + 1  # Increase depth since each player has moved
                val = max_value(next_board, new_depth)
            else:
                val = exp_value(next_board, depth)
            values[ind] = val
        return np.max(values)

    def exp_value(board, depth):
        # Check if win, lose, or max depth reached
        if board.terminal or depth == max_depth:
            return board.get_reward()

        possible_actions = board.get_legal_actions()  # Get possible actions
        values = np.zeros(len(possible_actions))  # Keep track of values corresp to actions
        for ind, action in enumerate(possible_actions):
            next_board = board.make_action(board.state, action, board.board_size)
            # Change player index
            if board.turn == 0:  # If pacman/player
                new_depth = depth + 1  # Increase depth since each player has moved
                val = max_value(next_board, new_depth)
            else:
                val = exp_value(next_board, depth)
            values[ind] = val
        return np.mean(values)

    return expectimax_decision(board)
