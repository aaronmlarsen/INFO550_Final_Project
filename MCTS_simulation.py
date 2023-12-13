from MCTS import *


def MCTS_v_Random(roll_iters, display=False, player_id=0, board_size=3, return_winner=False, data_run=False, tree=None, return_tree=False):
    if tree is None:
        tree = MCTS()
    board = Board(board_size=board_size)
    while True:
        if display:
            print(f"Person {board.turn + 1}")
        if player_id == 0:
            for _ in range(roll_iters):
                tree.rollout(board)
            next_action = tree.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
        if display:
            print(f"Person {board.turn + 1}")
        if player_id != 0:
            for _ in range(roll_iters):
                tree.rollout(board)
            next_action = tree.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
    if return_winner and not return_tree:
        return board.winner
    elif return_winner and return_tree:
        return board.winner, tree
    elif return_winner:
        return board.winner
    elif return_tree:
        return tree


def MCTS_v_MCTS(roll_iters, display=False, player_id=0, board_size=3, return_winner=False, data_run=False):
    tree1 = MCTS()
    tree2 = MCTS()

    board = Board(board_size=board_size)
    while True:
        if display:
            print(f"Person {board.turn + 1}")
        if player_id == 0:
            for _ in range(roll_iters):
                tree1.rollout(board)
            next_action = tree1.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            for _ in range(roll_iters):
                tree2.rollout(board)
            next_action = tree2.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        if display:
            show_tic_tac_toe(board.state)
            print()
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
        if display:
            print(f"Person {board.turn + 1}")
        if player_id != 0:
            for _ in range(roll_iters):
                tree1.rollout(board)
            next_action = tree1.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            for _ in range(roll_iters):
                tree2.rollout(board)
            next_action = tree2.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        if display:
            show_tic_tac_toe(board.state)
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
    if return_winner:
        return board.winner


def MCTS_v_Minimax(roll_iters, max_depth=2, display=False, player_id=0, board_size=3, return_winner=False, data_run=False):
    tree = MCTS()
    board = Board(board_size=board_size)
    while True:
        if display:
            print(f"Person {board.turn + 1}")
        if player_id == 0:
            for _ in range(roll_iters):
                tree.rollout(board)
            next_action = tree.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            next_action = minimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        if display:
            show_tic_tac_toe(board.state)
            print()
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
        if display:
            print(f"Person {board.turn + 1}")
        if player_id != 0:
            for _ in range(roll_iters):
                tree.rollout(board)
            next_action = tree.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            next_action = minimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        if display:
            show_tic_tac_toe(board.state)
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
    if return_winner:
        return board.winner


def Minimax_v_Random(max_depth=2, display=False, player_id=0, board_size=3, return_winner=False, data_run=False):
    board = Board(board_size=board_size)
    while True:
        if display:
            print(f"Person {board.turn + 1}")
        if player_id == 0:
            next_action = minimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
        if display:
            print(f"Person {board.turn + 1}")
        if player_id != 0:
            next_action = minimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
    if return_winner:
        return board.winner


def Expectimax_v_Random(max_depth=2, display=False, player_id=0, board_size=3, return_winner=False, data_run=False):
    board = Board(board_size=board_size)
    while True:
        if display:
            print(f"Person {board.turn + 1}")
        if player_id == 0:
            next_action = expectimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
        if display:
            print(f"Person {board.turn + 1}")
        if player_id != 0:
            next_action = expectimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
    if return_winner:
        return board.winner


def MCTS_v_Epectimax(roll_iters, max_depth=2, display=False, player_id=0, board_size=3, return_winner=False, data_run=False):
    tree = MCTS()
    board = Board(board_size=board_size)
    while True:
        for _ in range(roll_iters):
            tree.rollout(board)
        if display:
            print(f"Person {board.turn + 1}")
        if player_id == 0:
            for _ in range(roll_iters):
                tree.rollout(board)
            next_action = tree.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            next_action = expectimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        if display:
            show_tic_tac_toe(board.state)
            print()
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
        if display:
            print(f"Person {board.turn + 1}")
        if player_id != 0:
            for _ in range(roll_iters):
                tree.rollout(board)
            next_action = tree.choose_action(board)
            board = board.make_action(board.state, next_action, board.board_size)
        else:
            next_action = expectimax(board, max_depth)
            board = board.make_action(board.state, next_action, board.board_size)
        if display:
            show_tic_tac_toe(board.state)
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
    if return_winner:
        return board.winner


def Random_v_Random(display=False, player_id=0, board_size=3, return_winner=False, data_run=False):
    board = Board(board_size=board_size)
    while True:
        if display:
            print(f"Person {board.turn + 1}")
        if player_id == 0:
            board = board.random_child()
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
        if display:
            print(f"Person {board.turn + 1}")
        if player_id != 0:
            board = board.random_child()
        else:
            board = board.random_child()
        if display:
            show_tic_tac_toe(board.state)
            print()
        if board.terminal:
            if not display and not data_run:
                show_tic_tac_toe(board.state)
                print(f"Player {board.winner + 1} wins!")
            break
    if return_winner:
        return board.winner
