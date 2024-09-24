import tkinter as tk
from tkinter import messagebox

# Function to check if there is a winner and return the winning combination
def check_winner(board):
    # Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0], [(i, 0), (i, 1), (i, 2)]
    # Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i], [(0, i), (1, i), (2, i)]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0], [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2], [(0, 2), (1, 1), (2, 0)]
    return None, None

# This Function checks the board is full or not 
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    winner, _ = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

# This is Function to make the AI's move
def ai_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Initialize the Tic-Tac-Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

turn_label = tk.Label(root, text="Your Turn", font=('Arial', 20))
turn_label.grid(row=3, column=0, columnspan=3)

# This Set up the buttons for the grid
buttons = [[None for _ in range(3)] for _ in range(3)]
line_canvas = tk.Canvas(root, width=300, height=300, highlightthickness=0)
line_canvas.grid(row=0, column=0, rowspan=3, columnspan=3)

# it will handle the Function to handle button clicks
def on_click(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED)
        turn_label.config(text="AI's Turn")
        
        winner, combination = check_winner(board)
        if winner:
            draw_winning_line(combination)
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            reset_board()
            return

        if is_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
            return

        root.after(500, ai_move_wrapper)  # Delay AI's move slightly for better UX

# Function to make AI's move and check for a winner
def ai_move_wrapper():
    move = ai_move(board)
    if move:
        board[move[0]][move[1]] = 'O'
        buttons[move[0]][move[1]].config(text='O', state=tk.DISABLED)

    winner, combination = check_winner(board)
    if winner:
        draw_winning_line(combination)
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        reset_board()
        return

    if is_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        reset_board()
        return
    
    turn_label.config(text="Your Turn")

# Function to draw a line across the winning combination
def draw_winning_line(combination):
    x0, y0 = combination[0][1] * 100 + 50, combination[0][0] * 100 + 50
    x1, y1 = combination[2][1] * 100 + 50, combination[2][0] * 100 + 50
    line_canvas.create_line(x0, y0, x1, y1, width=4, fill='red')

# Function to reset the board
def reset_board():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state=tk.NORMAL)
    line_canvas.delete("all")
    turn_label.config(text="Your Turn")

# Create the buttons
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 40), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the Tkinter event loop
root.mainloop()
