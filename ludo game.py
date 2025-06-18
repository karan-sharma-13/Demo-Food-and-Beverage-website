import tkinter as tk
import random

class LudoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Ludo Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.create_board()
        self.player_pos = 0
        self.computer_pos = 0

        self.player_token = self.canvas.create_oval(30, 370, 50, 390, fill="blue")
        self.computer_token = self.canvas.create_oval(30, 350, 50, 370, fill="red")

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        self.status = tk.Label(root, text="Your Turn")
        self.status.pack()

    def create_board(self):
        for i in range(30):
            x = 30 + i * 35
            self.canvas.create_rectangle(x, 360, x + 35, 395, outline="black")
            self.canvas.create_rectangle(x, 320, x + 35, 355, outline="black")

    def move_token(self, token, steps, is_computer=False):
        for _ in range(steps):
            self.root.after(200)
            dx = 35
            self.canvas.move(token, dx, 0)
            self.canvas.update()

        if is_computer:
            self.status.config(text="Your Turn")
            self.roll_button.config(state="normal")
        else:
            self.root.after(1000, self.computer_turn)

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.status.config(text=f"You rolled a {roll}")
        self.roll_button.config(state="disabled")

        self.player_pos += roll
        self.move_token(self.player_token, roll, is_computer=False)

    def computer_turn(self):
        roll = random.randint(1, 6)
        self.status.config(text=f"Computer rolled a {roll}")
        self.computer_pos += roll
        self.move_token(self.computer_token, roll, is_computer=True)

# Start game
root = tk.Tk()
game = LudoGame(root)
root.mainloop()
