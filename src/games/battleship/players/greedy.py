import random
from random import randint
from random import choice
from games.battleship.action import BattleShipAction
from games.battleship.player import BattleShipPlayer
from games.battleship.state import BattleShipState
from games.state import State

class GreedyBattleShipPlayer(BattleShipPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: BattleShipState):
        grid = state.get_grid()

        selected_col = None
        max_count = 0

        for col in range(0, state.get_num_cols()):
            if not state.validate_action(BattleShipAction(col)):
                continue

            count = 0
            for row in range(0, state.get_num_rows()):
                if grid[row][col] == self.get_current_pos():
                    count += 1

            # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
            if selected_col is None or count > max_count or (count == max_count and choice([False, True])):
                selected_col = col
                max_count = count

        if selected_col is None:
            raise Exception("There is no valid action")

        return BattleShipAction(selected_col)

    def place_ships(board, num_ships):
        ship_count = 0
        while ship_count < num_ships:
            ship_row = random.randint(0, 9)
            ship_col = random.randint(0, 9)
            if board[ship_row][ship_col] == "0":
                board[ship_row][ship_col] = "S"
                ship_count += 1
        return board

    def take_turn(board, player):
        if player == "human":
            print("O seu truno")
            guess_row = int(input("Adivinhe a Coluna:"))
            guess_col = int(input("Adivinhe a linha"))
        else:
            print("Turno da maquina")
            guess_row = int(input("Adivinhe a linha:"))
            guess_col = int(input("Adivinhe a coluna"))
            print("Maquina escolhe uma linha: ", guess_row, "coluna", guess_col)
        if board[guess_row][guess_col] == "S":
            print("Parabens! Voce venceu")
            board[guess_row][guess_col] = "X"
        else:
            if guess_row not in range(10) or guess_col not in range(10):
                print("Posição inválida")
            elif board[guess_row][guess_col] == "X":
                print("O quadrado selecionado já foi jogado")
            else:
                print("Voce errou o navio adversário")
                board[guess_row][guess_col] = "X"
        return board


    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass