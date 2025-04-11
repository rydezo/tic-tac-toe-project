import random
import tkinter #GUI library for the game

x_player = "X"
y_player = "Y"
current_player = x_player

game_board = [[0, 0, 0], 
              [0, 0, 0], 
              [0, 0, 0]]

blue_color = "#7393B3"
orange_color = "#FFAC1C"
background = "#D3D3D3"

def set_tile(row, col):
    pass

def new_game():
    pass

#setup the window
window = tkinter.Tk()
window.title("Tic Tac Toe Game")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player+"'s turn!", font=("Helvetica", 20), 
                      background=background, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for col in range(3):
        game_board[row][col] = tkinter.Button(frame, text="", font=("Helvetica", 50, "bold"),
                                              background=background, foreground=blue_color,
                                              width=4, height=1, command=lambda row=row, column=col: set_tile(row, col))
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