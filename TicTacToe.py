import tkinter as tk
import random
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TicTacToe")
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font=("Arial", 40), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        print(self.buttons)


root = tk.Tk()
win = TicTacToe(root)
root.mainloop()
