from games.battleship.player import BattleShipPlayer
from games.battleship.state import BattleShipState
from games.game_simulator import GameSimulator


class BattleShipSimulator(GameSimulator):

    def __init__(self, player1: BattleShipPlayer, player2: BattleShipPlayer, num_rows: int = 6, num_cols: int = 7):
        super(BattleShipSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the battleship grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return BattleShipState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: BattleShipState):
        # ignored for this simulator
        pass

    def end_game(self, state: BattleShipState):
        # ignored for this simulator
        pass