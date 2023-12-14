from matplotlib import pyplot as plt
import numpy as np


def game_plots_MCTS_rollout(data, iters, roll_out, method2, filename):
    """Makes plot of wins with increasing rollouts and increasing alpha"""
    for i in range(roll_out):
        valArr1 = data[iters * i:iters * (i + 1), 3]
        valArr2 = data[iters * i:iters * (i + 1), 2]
        valArr3 = data[iters * i:iters * (i + 1), 4]

        conc1 = []
        conc2 = []
        conc3 = []
        for j in range(len(valArr1)):
            val = np.mean(valArr1[:j + 1])
            conc1.append(val)
            val = np.mean(valArr2[:j + 1])
            conc2.append(val)
            val = np.mean(valArr3[:j + 1])
            conc3.append(val)

        if i == 19:
            plt.plot(conc1, 'c', label="MCTS", alpha=1 / (roll_out - 1 - i + 1))
            plt.plot(conc2, 'r', label=method2, alpha=1 / (roll_out - 1 - i + 1))
            plt.plot(conc3, 'g', label="Draw", alpha=1 / (roll_out - 1 - i + 1))
        else:
            plt.plot(conc1, 'c', alpha=1 / (roll_out - 1 - i + 1))
            plt.plot(conc2, 'r', alpha=1 / (roll_out - 1 - i + 1))
            plt.plot(conc3, 'g', alpha=1 / (roll_out - 1 - i + 1))

    plt.xlabel("Game Number")
    plt.ylabel("Win Rate")
    plt.legend()
    plt.savefig(filename + "_games.jpeg", dpi=640, bbox_inches='tight')

    plt.clf()

    plt.plot(np.arange(20), data[:roll_out, 0] / iters, 'c', label="MCTS")
    plt.plot(np.arange(20), data[:roll_out, 1] / iters, 'r', label="Random")
    plt.plot(np.arange(20), data[:roll_out, 2] / iters, 'g', label="Draw")
    plt.xlabel("Number of Rollouts")
    plt.ylabel("Win Rate")
    plt.xticks(np.arange(roll_out), np.arange(roll_out) + 1)
    plt.legend()
    plt.savefig(filename + "_rollout.jpeg", dpi=640, bbox_inches='tight')


def game_plots_MCTS(data, iters, roll_out, method2, filename):
    """Makes plot of wins, loses, and draws"""
    for i in range(roll_out):
        valArr1 = data[iters * i:iters * (i + 1), 3]
        valArr2 = data[iters * i:iters * (i + 1), 2]
        valArr3 = data[iters * i:iters * (i + 1), 4]

        conc1 = []
        conc2 = []
        conc3 = []
        for j in range(len(valArr1)):
            val = np.mean(valArr1[:j + 1])
            conc1.append(val)
            val = np.mean(valArr2[:j + 1])
            conc2.append(val)
            val = np.mean(valArr3[:j + 1])
            conc3.append(val)

        plt.plot(conc1, 'c', label="MCTS")
        plt.plot(conc2, 'r', label=method2)
        plt.plot(conc3, 'g', label="Draw")

    plt.xlabel("Game Number")
    plt.ylabel("Win Rate")
    plt.legend()
    plt.savefig(filename + "_games.jpeg", dpi=640, bbox_inches='tight')


def game_plots(data, iters, method1, method2, filename):
    """Makes plot of wins, loses, and draws"""
    valArr1 = data[:, 0]
    valArr2 = data[:, 1]
    valArr3 = data[:, 2]

    conc1 = []
    conc2 = []
    conc3 = []
    for j in range(len(valArr1)):
        val = np.mean(valArr1[:j + 1])
        conc1.append(val)
        val = np.mean(valArr2[:j + 1])
        conc2.append(val)
        val = np.mean(valArr3[:j + 1])
        conc3.append(val)

    plt.plot(conc1, 'c', label=method1)
    plt.plot(conc2, 'r', label=method2)
    plt.plot(conc3, 'g', label="Draw")

    plt.xlabel("Game Number")
    plt.ylabel("Win Rate")
    plt.legend()
    plt.savefig(filename + "_games.jpeg", dpi=640, bbox_inches='tight')
