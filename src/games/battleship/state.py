import itertools
from typing import Optional

from games.battleship.action import BattleShipAction
from games.battleship.result import BattleShipResult
from games.state import State


class BattleShipState(State):
    EMPTY_CELL = -1

    def __init__(self):
        super().__init__()


        """
        the dimensions of the board
        """
        self.num_rows = 10
        self.num_cols = 10

        """
        the grid
        """
        self.grid = [[BattleShipState.EMPTY_CELL for _i in range(self.num_cols)] for _j in range(self.num_rows)]
        self.grid1 = [[BattleShipState.EMPTY_CELL for _i in range(self.num_cols)] for _j in range(self.num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: BattleShipAction) -> bool:
        col = action.get_col()


        # valid column
        if col < 0 or col >= self.num_cols:
            return False

        # full column
        if self.grid[0][col] != BattleShipState.EMPTY_CELL:
            return False

        return True

    def update(self, action: BattleShipAction):
        col = action.get_col()

        # drop the checker
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__grid[row][col] < 0:
                self.__grid[row][col] = self.__acting_player
                break

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'X',
                  1: 'O',
                  BattleShipState.EMPTY_CELL: ' '
              }[self.grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.num_rows):
            print('|', end="")
            for col in range(0, self.num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.num_cols * self.num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = BattleShipState(self.num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                cloned_state.grid[row][col] = self.grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[BattleShipResult]:
        if self.__has_winner:
            return BattleShipResult.LOOSE if pos == self.__acting_player else BattleShipResult.WIN
        if self.__is_full():
            return BattleShipResult.DRAW
        return None

    def get_num_rows(self):
        return self.num_rows

    def get_num_cols(self):
        return self.num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda position: BattleShipAction(position[0], position[1]),
                itertools.product(range(0, self.get_num_rows()),
                                  range(0, self.get_num_cols())))
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
