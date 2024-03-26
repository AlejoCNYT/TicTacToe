# Autor: Daniel Alejandro Acero
# Fecha: 25/03/2024
# Descripción: Juego de Tic Tac (Triqui). Dinamic Programming.

import numpy as np

# Definir el tamaño del tablero
N = 3

# Definir los símbolos para los jugadores
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (N*2-1))

# Función para verificar si el tablero está lleno
def is_board_full(board):
    return not any(EMPTY in row for row in board)

# Función para verificar si un jugador ha ganado
def check_winner(board, player):
    # Verificar filas y columnas
    for i in range(N):
        if all(board[i][j] == player for j in range(N)) or all(board[j][i] == player for j in range(N)):
            return True
    # Verificar diagonales
    if all(board[i][i] == player for i in range(N)) or all(board[i][N-1-i] == player for i in range(N)):
        return True
    return False

# Función para determinar si el juego ha terminado
def game_over(board):
    return is_board_full(board) or check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O)

# Función para obtener los movimientos válidos
def get_valid_moves(board):
    valid_moves = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == EMPTY:
                valid_moves.append((i, j))
    return valid_moves

# Función para evaluar la posición actual
def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    else:
        return 0

# Función para determinar el mejor movimiento usando programación dinámica (minimax)
def minimax(board, depth, maximizing_player):
    if game_over(board) or depth == 0:
        return evaluate(board)

    valid_moves = get_valid_moves(board)
    if maximizing_player:
        max_eval = float('-inf')
        for move in valid_moves:
            i, j = move
            board[i][j] = PLAYER_X
            eval = minimax(board, depth - 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in valid_moves:
            i, j = move
            board[i][j] = PLAYER_O
            eval = minimax(board, depth - 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

# Función para determinar el mejor movimiento para la computadora
def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    valid_moves = get_valid_moves(board)
    for move in valid_moves:
        i, j = move
        board[i][j] = PLAYER_X
        eval = minimax(board, 10, False) # Profundidad arbitraria, podría ser ajustada
        board[i][j] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Función principal para jugar al juego
def play_game():
    board = np.full((N, N), EMPTY, dtype=str)
    current_player = PLAYER_X

    while not game_over(board):
        print_board(board)
        if current_player == PLAYER_X:
            i, j = map(int, input("Ingrese su movimiento (fila y columna, separados por espacio): ").split())
            if board[i][j] != EMPTY:
                print("Movimiento inválido. Inténtelo de nuevo.")
                continue
            board[i][j] = current_player
        else:
            print("Turno de la computadora:")
            i, j = get_best_move(board)
            board[i][j] = current_player

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    print_board(board)
    if check_winner(board, PLAYER_X):
        print("¡Has ganado!")
    elif check_winner(board, PLAYER_O):
        print("La computadora ha ganado.")
    else:
        print("Empate.")

# Iniciar el juego
play_game()
