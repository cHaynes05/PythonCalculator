import tkinter as tk
from tkinter import font as tkfont
from constants import *

class TIPYUI:
    def __init__(self, root, calculator):
        self.root = root
        self.calculator = calculator
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.root.title("TI-PY Calculator")
        self.root.geometry(f"{CALC_WIDTH}x{CALC_HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg="#1A1A2E")

    def create_widgets(self):
        # Main container
        container = tk.Frame(self.root, bg="#1A1A2E", padx=10, pady=10)
        container.pack(fill=tk.BOTH, expand=True)

        # Display
        self.create_display(container)

        # Buttons
        self.create_buttons(container)

    def create_display(self, parent):
        display_frame = tk.Frame(parent, bg=DISPLAY_BG, relief=tk.SUNKEN, bd=2)
        display_frame.pack(pady=(10, 20), fill=tk.X)

        # Display text
        self.display = tk.Label(
            display_frame,
            text="0",
            bg=DISPLAY_BG,
            fg=DISPLAY_FG,
            font=("Courier", 20, "bold"),
            anchor="e",
            padx=10,
            pady=10,
            height=3
        )
        self.display.pack(fill=tk.BOTH, expand=True)

    def create_buttons(self, parent):
        button_frame = tk.Frame(parent, bg="#1A1A2E")
        button_frame.pack(fill=tk.BOTH, expand=True)

        for row_idx, row in enumerate(BUTTON_LAYOUT):
            for col_idx, (text, color) in enumerate(row):
                if text == "":
                    continue

                btn = tk.Button(
                    button_frame,
                    text=text,
                    bg=color,
                    fg="white",
                    font=("Arial", 10, "bold"),
                    width=8,
                    height=2,
                    relief=tk.RAISED,
                    bd=3,
                    command=lambda t=text: self.button_click(t)
                )

                # Make ENTER button wider
                if text == "ENTER":
                    btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky="nsew", columnspan=1)
                else:
                    btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky="nsew")

        # Configure grid weights
        for i in range(5):
            button_frame.columnconfigure(i, weight=1)
        for i in range(len(BUTTON_LAYOUT)):
            button_frame.rowconfigure(i, weight=1)

    def button_click(self, text):
        # Clear error state when entering new input
        if self.calculator.display_text == "ERROR" and text not in ["CLR", "DEL"]:
            self.calculator.clear_display()

        if text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.calculator.add_to_display(text)
        elif text == ".":
            self.calculator.add_to_display(".")
        elif text in ["+", "−", "×", "÷"]:
            self.calculator.add_to_display(text)
        elif text == "^":
            self.calculator.add_to_display("^")
        elif text == "(":
            self.calculator.add_to_display("(")
        elif text == ")":
            self.calculator.add_to_display(")")
        elif text == ",":
            self.calculator.add_to_display(",")
        elif text == "ENTER":
            self.calculator.calculate()
        elif text == "CLR":
            self.calculator.clear_display()
        elif text == "DEL":
            self.calculator.delete_last()
        elif text == "(−)":
            self.calculator.negate()
        elif text == "SIN":
            self.calculator.add_to_display("SIN(")
        elif text == "COS":
            self.calculator.add_to_display("COS(")
        elif text == "TAN":
            self.calculator.add_to_display("TAN(")
        elif text == "LOG":
            self.calculator.add_to_display("LOG(")
        elif text == "LN":
            self.calculator.add_to_display("LN(")
        elif text == "X²":
            self.calculator.add_to_display("^2")
        elif text == "X⁻¹":
            self.calculator.add_to_display("^(-1)")

        self.update_display()

    def update_display(self):
        display_text = self.calculator.display_text if self.calculator.display_text else "0"
        self.display.config(text=display_text)
