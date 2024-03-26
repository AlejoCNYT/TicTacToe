# Autor: Daniel Alejandro Acero
# Fecha: 25/03/2024
# Descripción: Juego de Tic Tac (Triqui). DFS/Recursive.

class TicTacToeDFS:
    @staticmethod
    def dfs(game, player, max_depth=9, current_depth=0):
        """
        Depth-First Search to iterate through the game tree
        :param game: TicTacToe instance
        :param player: Player instance ('X' or 'O')
        :param max_depth: Maximum depth to search (default: 9, considering maximum 9 moves in Tic Tac Toe)
        :param current_depth: Current depth in the tree (default: 0)
        """
        if current_depth >= max_depth or game.current_winner is not None:
            # If maximum depth is reached or there's a winner, stop the search
            return

        for move in game.available_moves():
            # Iterate through available moves
            game_copy = TicTacToe()
            game_copy.board = game.board[:]  # Create a copy of the board
            game_copy.current_winner = game.current_winner  # Copy the current winner
            game_copy.make_move(move, player)  # Make a move

            print(f"Move: {move}, Player: {player}, Depth: {current_depth}")
            game_copy.print_board()

            # Switch player and continue searching
            next_player = 'O' if player == 'X' else 'X'
            TicTacToeDFS.dfs(game_copy, next_player, max_depth, current_depth + 1)

if __name__ == '__main__':
    game = TicTacToe()
    TicTacToeDFS.dfs(game, 'X')
