# Display settings
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 120
DISPLAY_BG = "#9DB4AB"
DISPLAY_FG = "#000000"

# Calculator dimensions
CALC_WIDTH = 450
CALC_HEIGHT = 650

# Button colors (matching TI-84)
BTN_DARK_BLUE = "#1A365D"
BTN_LIGHT_BLUE = "#4A90E2"
BTN_GRAY = "#7B8794"
BTN_BLACK = "#2D3748"
BTN_GREEN = "#38A169"

# Button layout - Simplified functional buttons only
BUTTON_LAYOUT = [
    # Row 1 - Top functions
    [("DEL", BTN_DARK_BLUE), ("CLR", BTN_DARK_BLUE), ("", None), ("", None), ("", None)],

    # Row 2 - Math functions
    [("SIN", BTN_GRAY), ("COS", BTN_GRAY), ("TAN", BTN_GRAY), ("^", BTN_GRAY), ("X⁻¹", BTN_GRAY)],

    # Row 3 - More math functions
    [("LOG", BTN_GRAY), ("LN", BTN_GRAY), ("X²", BTN_GRAY), ("(", BTN_GRAY), (")", BTN_GRAY)],

    # Row 4 - Numbers and operators
    [("7", BTN_BLACK), ("8", BTN_BLACK), ("9", BTN_BLACK), ("÷", BTN_GRAY), ("×", BTN_GRAY)],

    # Row 5
    [("4", BTN_BLACK), ("5", BTN_BLACK), ("6", BTN_BLACK), ("−", BTN_GRAY), ("+", BTN_GRAY)],

    # Row 6
    [("1", BTN_BLACK), ("2", BTN_BLACK), ("3", BTN_BLACK), (".", BTN_BLACK), ("(−)", BTN_BLACK)],

    # Row 7
    [("0", BTN_BLACK), ("", None), ("", None), ("", None), ("ENTER", BTN_LIGHT_BLUE)]
]
