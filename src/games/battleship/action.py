class BattleShipAction:
    __col: int
    __row: int

    def __init__(self, col: int):
        self.__col = col


    def get_col(self):
        return self.__col


