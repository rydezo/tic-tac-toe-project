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

#setup the window
window = tkinter.Tk()
window.title("Tic Tac Toe Game")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player+"'s turn!", font=("Helvetica", 20), 
                      background=background, foreground="white")

label.grid(row=0, column=0)

for row in range(3):
    for col in range(3):
        game_board[row][col] = tkinter.Button(frame, text="", font=("Helvetica", 50, "bold"),
                                              background=background, foreground=blue_color,
                                              width=4, height=1, command=lambda row=row, column=col: set_tile(row, col))
        game_board[row][col].grid(row=row+1, column=col)

frame.pack()

window.mainloop()