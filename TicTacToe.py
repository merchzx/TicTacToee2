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
        self.winBoards = [
            ('X', 'X', 'X', '', '', '', '', '', '')
            , ('', '', '', 'X', 'X', 'X', '', '', '')
            , ('', '', '', '', '', '', 'X', 'X', 'X')
            , ('X', '', '', 'X', '', '', 'X', '', '')
            , ('', 'X', '', '', 'X', '', '', 'X', '')
            , ('', '', 'X', '', '', 'X', '', '', 'X')
            , ('X', '', '', '', 'X', '', '', '', 'X')
            , ('', '', 'X', '', 'X', '', 'X', '', '')
        ]

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font=("Arial", 40), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            self.grid = button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        print(self.buttons[index])
        randomNumber = random.randint(1, 9)
        if self.board[index] == '':
            self.board[index] = 'X'
            self.buttons[index].config(text='X')
            if self.check_info('X'):
                messagebox.showinfo("Game Over", "You Win")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "Draw")
                self.reset_game()
            else:
                self.root.after(0, self.comp_move(index))

    def comp_move(self, index):
        empty_ind = [i for i, v in enumerate(self.board) if "" == v]
        if not empty_ind:
            return
        randomNumber = random.choice(empty_ind)
        self.board[randomNumber] = 'O'
        self.buttons[randomNumber].config(text='O')
        if self.check_info('O'):
            messagebox.showinfo("Game Over", "Comp Win")
            self.reset_game()
        elif "" not in self.board:
            messagebox.showinfo("Game Over", "Draw")
            self.reset_game()

    def check_info(self, symb):
        # for i in self.winBoards:
        #     for j,k,l in self.winBoards[i]:
        #         if j =='X' and k =='X' and l =='X':
        #             pass

        combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (6, 4, 2)
                  ]
        for a, b, c in combos:
            print(a, b, c)
            if self.board[a] == self.board[b] == self.board[c] == symb:
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="")


root = tk.Tk()
win = TicTacToe(root)
root.mainloop()
