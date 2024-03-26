# Autor: Daniel Alejandro Acero
# Fecha: 25/03/2024
# Descripción: Juego de Tic Tac (Triqui). BFS.

import random  # Importa el módulo random para generar números aleatorios

class TicTacToe:
    def __init__(self):
        # Inicializa el juego con un tablero vacío y sin ganador actual
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # Imprime el tablero en la consola
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Devuelve una lista de índices de las casillas disponibles en el tablero
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def num_empty_squares(self):
        # Devuelve el número de casillas vacías en el tablero
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Realiza un movimiento en el tablero si la casilla especificada está vacía
        if self.board[square] == ' ':
            self.board[square] = letter
            # Comprueba si el movimiento actual ha llevado a una victoria
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Comprueba si el jugador actual ha ganado después del último movimiento
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    # Función principal para jugar una partida de Tic Tac Toe
    if print_game:
        game.print_board()

    letter = 'X'  # Empieza el jugador X
    while game.num_empty_squares() > 0:
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'  # Cambia el turno del jugador

    if print_game:
        print("It's a tie!")

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        # Solicita al jugador humano que ingrese un movimiento válido
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        # La IA selecciona un movimiento aleatorio de entre los movimientos disponibles
        return random.choice(game.available_moves())

if __name__ == '__main__':
    # Configura los jugadores y comienza la partida
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
