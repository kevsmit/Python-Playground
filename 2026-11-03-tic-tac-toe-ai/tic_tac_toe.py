"""Tic-tac-toe against the computer. The computer uses minimax, so it never loses."""

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def winner(board):
    for a, b, c in WINS:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def minimax(board, player):
    """Return a score from the computer's (O) point of view: +1 win, 0 draw, -1 loss."""
    w = winner(board)
    if w == "O":
        return 1
    if w == "X":
        return -1
    if " " not in board:
        return 0
    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            scores.append(minimax(board, "X" if player == "O" else "O"))
            board[i] = " "
    return max(scores) if player == "O" else min(scores)


def best_move(board):
    best, move = -2, None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, "X")
            board[i] = " "
            if score > best:
                best, move = score, i
    return move


def show(board):
    for r in range(3):
        print(" " + " | ".join(board[r * 3:r * 3 + 3]))
        if r < 2:
            print("---+---+---")


def main():
    board = [" "] * 9
    print("You are X. Enter a square number 1-9 (left to right, top to bottom).")
    while True:
        show(board)
        try:
            move = int(input("Your move: ")) - 1
        except ValueError:
            print("Please enter a number.")
            continue
        if move not in range(9) or board[move] != " ":
            print("That square isn't available.")
            continue
        board[move] = "X"
        if winner(board) or " " not in board:
            break
        board[best_move(board)] = "O"
        if winner(board) or " " not in board:
            break
    show(board)
    result = winner(board)
    print(f"{result} wins!" if result else "It's a draw.")


if __name__ == "__main__":
    main()
