import random
from games.battleship.action import BattleShipAction
from games.battleship.player import BattleShipPlayer
from games.battleship.state import BattleShipState


BOARD_SIZE = 10
SHIP_SIZES = [5, 4, 3, 3, 2]
board = [['O' for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

class HumanBattleShipPlayer(BattleShipPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: BattleShipState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return BattleShipAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")))
            except Exception:
                continue


    def place_ship(board, ship_size):
        while True:
            row = random.randint(0, BOARD_SIZE-1)
            col = random.randint(0, BOARD_SIZE-1)
            is_horizontal = random.choice([True, False])

            if(is_horizontal and col + ship_size <= BOARD_SIZE) or (not is_horizontal and row + ship_size <= BOARD_SIZE):
                for i in range(ship_size):
                    if is_horizontal:
                        board[row][col+i] = 'S'
                    else:
                        board[row+i][col] = 'S'
                break

    for ship_size in SHIP_SIZES:
        place_ship(board, ship_size)


    def display_board(board):
        print(' '+' '.join(str(i) for i in range(BOARD_SIZE)))
        for i in range(BOARD_SIZE):
            print(str(i)+' '+' '.join(board[i]))

    def get_move(board):
        while True:
            try:
                move = input('Enter your move: ')
                row, col = move.split(',')
                row = int(row)
                col = int(col)
                if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                    raise ValueError
                break
            except ValueError:
                print('Invalid move. Try again')
        return row, col

    while True:
        display_board(board)

        print('Player 1, make your move:')
        row, col = get_move()
        if board[row][col] == 'S':
            print('Hit!')
            board[row][col] = 'X'
        else:
            print('Miss')

        if all('S' not in row for row in board):
            print('Player 1 wins!')
            break

        display_board(board)

        print('Player 2, make your move:')
        row, col = get_move()
        if board[row][col] == 'S':
            print('Hit!')
            board[row][col] = 'X'
        else:
            print('Miss!')

        if all('S' not in row for row in board):
            print('Player 2 wins!')
            break


    def event_action(self, pos: int, action, new_state: BattleShipState):
        # ignore
        pass

    def event_end_game(self, final_state: BattleShipState):
        # ignore
        pass
