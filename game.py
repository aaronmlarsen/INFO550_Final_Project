from MCTS_simulation import *
from tqdm import tqdm
from game_plots import *

test_iters = 1000
num_roll_outs = 10

player_ids = np.random.randint(2, size=test_iters)

board_sizes = [3]

"""Make plots of Agent vs Agent"""
for board_size in board_sizes:
    """MCTS vs Random Agent"""
    MCTS_random = np.zeros(3)
    MCTS_random_games = np.zeros((test_iters, 3))
    for i in tqdm(range(test_iters)):
        winner = MCTS_v_Random(num_roll_outs, player_id=player_ids[i], return_winner=True, data_run=True,
                               board_size=board_size)
        if (winner == 2) or (player_ids[i] == 0):
            MCTS_random[winner] += 1
            MCTS_random_games[i, winner] = 1
        elif player_ids[i] == 1 and winner == 1:
            MCTS_random[winner - 1] += 1
            MCTS_random_games[i, winner - 1] = 1
        elif player_ids[i] == 1 and winner == 0:
            MCTS_random[winner + 1] += 1
            MCTS_random_games[i, winner + 1] = 1
    game_plots(MCTS_random_games, test_iters, "MCTS", "Random",
               f"MCTS_random_{test_iters}_{num_roll_outs}_{board_size}")

    """MCTS vs MCTS"""
    MCTS_MCTS = np.zeros(3)
    MCTS_MCTS_games = np.zeros((test_iters, 3))
    for i in tqdm(range(test_iters)):
        winner = MCTS_v_MCTS(10, player_id=player_ids[i], return_winner=True, data_run=True, board_size=board_size)
        if (winner == 2) or (player_ids[i] == 0):
            MCTS_MCTS[winner] += 1
            MCTS_MCTS_games[i, winner] = 1
        elif player_ids[i] == 1 and winner == 0:
            MCTS_MCTS[winner + 1] += 1
            MCTS_MCTS_games[i, winner + 1] = 1
        elif player_ids[i] == 1 and winner == 1:
            MCTS_MCTS[winner - 1] += 1
            MCTS_MCTS_games[i, winner - 1] = 1
    game_plots(MCTS_MCTS_games, test_iters, "MCTS 1", "MCTS 2", f"MCTS_MCTS_{test_iters}_{num_roll_outs}_{board_size}")

    """MCTS vs Minimax"""
    MCTS_Minimax = np.zeros(3)
    MCTS_Minimax_games = np.zeros((test_iters, 3))
    for i in tqdm(range(test_iters)):
        winner = MCTS_v_Minimax(10, player_id=player_ids[i], return_winner=True, data_run=True, board_size=board_size)
        if (winner == 2) or (player_ids[i] == 0):
            MCTS_Minimax[winner] += 1
            MCTS_Minimax_games[i, winner] = 1
        elif player_ids[i] == 1 and winner == 0:
            MCTS_Minimax[winner + 1] += 1
            MCTS_Minimax_games[i, winner + 1] = 1
        elif player_ids[i] == 1 and winner == 1:
            MCTS_Minimax[winner - 1] += 1
            MCTS_Minimax_games[i, winner - 1] = 1
    game_plots(MCTS_Minimax_games, test_iters, "MCTS", "Minimax",
               f"MCTS_Minimax_{test_iters}_{num_roll_outs}_{board_size}")

    """Minimax vs Random Agent"""
    Minimax_random = np.zeros(3)
    Minimax_random_games = np.zeros((test_iters, 3))
    for i in tqdm(range(test_iters)):
        winner = Minimax_v_Random(player_id=player_ids[i], return_winner=True, data_run=True, board_size=board_size)
        if (winner == 2) or (player_ids[i] == 0):
            Minimax_random[winner] += 1
            Minimax_random_games[i, winner] = 1
        elif player_ids[i] == 1 and winner == 0:
            Minimax_random[winner + 1] += 1
            Minimax_random_games[i, winner + 1] = 1
        elif player_ids[i] == 1 and winner == 1:
            Minimax_random[winner - 1] += 1
            Minimax_random_games[i, winner - 1] = 1
    game_plots(Minimax_random_games, test_iters, "Minimax", "Random", f"Minimax_Random_{test_iters}_{board_size}")

    """Expectimax vs Random Agent"""
    Expectimax_random = np.zeros(3)
    Expectimax_random_games = np.zeros((test_iters, 3))
    for i in tqdm(range(test_iters)):
        winner = Expectimax_v_Random(player_id=player_ids[i], return_winner=True, data_run=True, board_size=board_size)
        if (winner == 2) or (player_ids[i] == 0):
            Expectimax_random[winner] += 1
            Expectimax_random_games[i, winner] = 1
        elif player_ids[i] == 1 and winner == 0:
            Expectimax_random[winner + 1] += 1
            Expectimax_random_games[i, winner + 1] = 1
        elif player_ids[i] == 1 and winner == 1:
            Expectimax_random[winner - 1] += 1
            Expectimax_random_games[i, winner - 1] = 1
    game_plots(Expectimax_random_games, test_iters, "Expectimax", "Random",
               f"Expctimax_Random_{test_iters}_{board_size}")

    """MCTS vs Expectimax"""
    MCTS_Expectimax = np.zeros(3)
    MCTS_Expectimax_games = np.zeros((test_iters, 3))
    for i in tqdm(range(test_iters)):
        winner = MCTS_v_Epectimax(10, player_id=player_ids[i], return_winner=True, data_run=True, board_size=board_size)
        if (winner == 2) or (player_ids[i] == 0):
            MCTS_Expectimax[winner] += 1
            MCTS_Expectimax_games[i, winner] = 1
        elif player_ids[i] == 1 and winner == 0:
            MCTS_Expectimax[winner + 1] += 1
            MCTS_Expectimax_games[i, winner + 1] = 1
        elif player_ids[i] == 1 and winner == 1:
            MCTS_Expectimax[winner - 1] += 1
            MCTS_Expectimax_games[i, winner - 1] = 1

    game_plots(MCTS_Expectimax_games, test_iters, "MCTS", "Expectimax",
               f"MCTS_Expectimax_{test_iters}_{num_roll_outs}_{board_size}")

    """Random Agent vs Random Agent"""
    Random_Random = np.zeros(3)
    Random_Random_games = np.zeros((test_iters, 3))
    for i in tqdm(range(test_iters)):
        winner = Random_v_Random(player_id=player_ids[i], return_winner=True, data_run=True, board_size=board_size)
        if (winner == 2) or (player_ids[i] == 0):
            Random_Random[winner] += 1
            Random_Random_games[i, winner] = 1
        elif player_ids[i] == 1 and winner == 0:
            Random_Random[winner + 1] += 1
            Random_Random_games[i, winner + 1] = 1
        elif player_ids[i] == 1 and winner == 1:
            Random_Random[winner - 1] += 1
            Random_Random_games[i, winner - 1] = 1
    game_plots(Random_Random_games, test_iters, "Random 1", "Random 2", f"Random_Random_{test_iters}_{board_size}")

"""Make plots of increasing rollout number"""
board_sizes = [3, 5]
for board_size in board_sizes:

    test_iters = 2000
    max_roll_outs = 20
    player_ids = np.random.randint(2, size=test_iters)

    MCTS_random_rollout = np.zeros((max_roll_outs, 3))
    MCTS_random_rollout_results = np.zeros((test_iters * max_roll_outs, 5))
    ctr = 0
    for iters in tqdm(range(1, max_roll_outs + 1)):
        for i in range(test_iters):
            if ctr == 0:
                winner, tree = MCTS_v_Random(iters, player_id=player_ids[i], return_winner=True, data_run=True,
                                             board_size=board_size, return_tree=True)
            else:
                winner, tree = MCTS_v_Random(iters, player_id=player_ids[i], return_winner=True, data_run=True,
                                             board_size=board_size, tree=tree, return_tree=True)
            if (winner == 2) or (player_ids[i] == 0):
                MCTS_random_rollout[iters - 1, winner] += 1
                MCTS_random_rollout_results[ctr, winner + 2] = 1
            elif player_ids[i] == 1 and winner == 0:
                MCTS_random_rollout[iters - 1, winner + 1] += 1
                MCTS_random_rollout_results[ctr, winner + 3] = 1
            elif player_ids[i] == 1 and winner == 1:
                MCTS_random_rollout[iters - 1, winner - 1] += 1
                MCTS_random_rollout_results[ctr, winner + 2] = 1
            MCTS_random_rollout_results[ctr, 0] = iters
            MCTS_random_rollout_results[ctr, 1] = i
            ctr += 1

    game_plots_MCTS_rollout(MCTS_random_rollout_results, test_iters, max_roll_outs, "Random",
                            f"as_rollouts_increase_tree_save_{board_size}")
    game_plots_MCTS(MCTS_random_rollout_results, test_iters, max_roll_outs, "Random",
                    f"as_rollouts_increase_all_tree_save_{board_size}")
