import random

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Function to check for a draw
def is_draw(board):
    return ' ' not in board

# Computer move
def computer_move(board):
    empty_positions = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(empty_positions)

# Main game
def play_game():
    board = [' '] * 9
    user = 'X'
    computer = 'O'

    print("🎮 Welcome to Tic-Tac-Toe!")
    print("You are X. Computer is O.")
    display_board(board)

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[move] = user
        display_board(board)

        if check_win(board, user):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

        print("Computer's turn...")
        comp_move = computer_move(board)
        board[comp_move] = computer
        display_board(board)

        if check_win(board, computer):
            print("💻 Computer wins! Better luck next time.")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play_game()
