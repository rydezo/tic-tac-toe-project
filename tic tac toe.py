import random
import tkinter #GUI library for the game

def set_tile(row, col):
    global current_player

    if game_board[row][col]["text"] != "":
        # if spot is already taken
        return
    
    game_board[row][col]["text"] = current_player

    # alternate the players
    if current_player == o_player:
        current_player = x_player
    else:
        current_player = o_player

    label["text"] = current_player + "'s turn"

    #check winning conditions
    check_winner()

def check_winner():
    global turns
    global game_over
    turns +=1

    #check horizontally
    for row in range(3):
        if (game_board[row][0]["text"] == game_board[row][1]["text"] 
            == game_board[row][2]["text"] and game_board[row][0]["text"] != ""):
            label.config(text=game_board[row][0]["text"] + " is the winner!", foreground=orange_color)
            # add color effect to winning arrangement
            for col in range(3):
                game_board[row][col].config(foreground=orange_color, background=background)
            game_over = True
            return

def new_game():
    pass

#setup players and board
x_player = "X"
o_player = "O"
current_player = x_player

game_board = [[0, 0, 0], 
              [0, 0, 0], 
              [0, 0, 0]]

blue_color = "#7393B3"
orange_color = "#FF8C00"
background = "#D3D3D3"

#game conditions
turns = 0
game_over = False

#setup the window
window = tkinter.Tk()
window.title("Tic Tac Toe Game")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player+"'s turn!", font=("Helvetica", 20), 
                      background=background, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

#setup each square
for row in range(3):
    for col in range(3):
        game_board[row][col] = tkinter.Button(frame, text="", font=("Helvetica", 50, "bold"),
                                              background=background, foreground=blue_color,
                                              width=4, height=1, command=lambda row=row, col=col: set_tile(row, col))
        game_board[row][col].grid(row=row+1, column=col)

button = tkinter.Button(frame, text="restart", font=("Helvetica", 20), background = background,
                        foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# center the game window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# format "(w)x(h)+x+y"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()