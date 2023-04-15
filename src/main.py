from games.battleship.players.greedy import GreedyBattleshipPlayer
from games.battleship.players.random import RandomBattleshipPlayer
from games.battleship.simulator import BattleshipSimulator
from games.game_simulator import GameSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1000

    c4_simulations = [
        # uncomment to play as human
        #{
        #    "name": "Connect4 - Human VS Random",
        #    "player1": HumanConnect4Player("Human"),
        #    "player2": RandomConnect4Player("Random")
        #},
        {
            "name": "Battleship - Random VS Random",
            "player1": RandomBattleshipPlayer("Random 1"),
            "player2": RandomBattleshipPlayer("Random 2")
        },
        {
            "name": "Battleship - Greedy VS Random",
            "player1": GreedyBattleshipPlayer("Greedy"),
            "player2": RandomBattleshipPlayer("Random")
        },
        {
            "name": "Minimax VS Random",
            "player2": RandomBattleshipPlayer("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player2": GreedyBattleshipPlayer("Greedy")
        }
    ]

    for sim in c4_simulations:
        run_simulation(sim["name"], BattleshipSimulator(sim["player1"], sim["player2"]), num_iterations)

if __name__ == "__main__":
    main()

