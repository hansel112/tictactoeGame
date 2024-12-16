#!/usr/bin/env python3

"""A python script for a tic-tac-toe game by Hansel Carzerlet

"""

import tkinter as tk
from tkinter import messagebox

ALL_SPACES = list('123456789')
X, O, BLANK = 'X', 'O', ' '

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.currentPlayer = X
        self.gameBoard = self.getBlankBoard()

        # Creating buttons for each cell on the board
        self.buttons = {}
        for i in range(1, 10):
            button = tk.Button(root, text=BLANK, font=('Helvetica', 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=(i-1)//3, column=(i-1)%3)
            self.buttons[str(i)] = button

        self.reset_button = tk.Button(root, text="Reset", font=('Helvetica', 12), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def getBlankBoard(self):
        """Creating a new, blank tic tac toe board."""
        board = {}
        for space in ALL_SPACES:
            board[space] = BLANK
        return board

    def reset_game(self):
        """Reseting the game board and buttons for a new game."""
        self.gameBoard = self.getBlankBoard()
        self.currentPlayer = X
        for button in self.buttons.values():
            button.config(text=BLANK, state=tk.NORMAL)

    def make_move(self, space):
        """Handling a player's moves."""
        space = str(space)
        if self.isValidSpace(space):
            self.updateBoard(space, self.currentPlayer)
            self.buttons[space].config(text=self.currentPlayer, state=tk.DISABLED)
            
            if self.isWinner(self.currentPlayer):
                messagebox.showinfo("Game Over", f"{self.currentPlayer} has won the game!")
                self.end_game()
            elif self.isBoardFull():
                messagebox.showinfo("Game Over", "The game is a tie!")
                self.end_game()
            else:
                # Switch players
                self.currentPlayer = O if self.currentPlayer == X else X

    def isValidSpace(self, space):
        """Returning True if the space on the board is a valid space and is blank."""
        return space in ALL_SPACES and self.gameBoard[space] == BLANK

    def isWinner(self, player):
        """Returning True if player has won on the current board."""
        b, p = self.gameBoard, player
        return ((b['1'] == b['2'] == b['3'] == p) or  # Across the top
                (b['4'] == b['5'] == b['6'] == p) or  # Across the middle
                (b['7'] == b['8'] == b['9'] == p) or  # Across the bottom
                (b['1'] == b['4'] == b['7'] == p) or  # Down the left
                (b['2'] == b['5'] == b['8'] == p) or  # Down the middle
                (b['3'] == b['6'] == b['9'] == p) or  # Down the right
                (b['1'] == b['5'] == b['9'] == p) or  # Diagonal
                (b['3'] == b['5'] == b['7'] == p))    # Diagonal

    def isBoardFull(self):
        """Returning True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self.gameBoard[space] == BLANK:
                return False
        return True

    def updateBoard(self, space, mark):
        """Setting the space on the board to the player's mark."""
        self.gameBoard[space] = mark

    def end_game(self):
        """Ending the game by disabling all buttons."""
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

