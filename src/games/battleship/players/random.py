from random import randint

from games.battleship.action import BattleShipAction
from games.battleship.player import BattleShipPlayer
from games.battleship.state import BattleShipState
from games.state import State


class RandomBattleShipPlayer(BattleShipPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: BattleShipState):
        return BattleShipAction(randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
