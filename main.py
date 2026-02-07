import tkinter as tk
from calculator import TIPYCalculator
from ui import TIPYUI

def main():
    root = tk.Tk()
    calculator = TIPYCalculator()
    ui = TIPYUI(root, calculator)
    root.mainloop()

if __name__ == "__main__":
    main()
