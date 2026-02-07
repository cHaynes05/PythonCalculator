import math
import re

class TIPYCalculator:
    def __init__(self):
        self.display_text = ""
        self.result = None
        self.memory = {}
        self.mode = "normal"  # normal, 2nd, alpha
        self.angle_mode = "rad"  # rad or deg

    def add_to_display(self, text):
        self.display_text += text

    def clear_display(self):
        self.display_text = ""
        self.result = None

    def delete_last(self):
        self.display_text = self.display_text[:-1]

    def calculate(self):
        try:
            # Replace calculator symbols with Python operators
            expression = self.display_text
            expression = expression.replace("×", "*")
            expression = expression.replace("÷", "/")
            expression = expression.replace("−", "-")
            expression = expression.replace("^", "**")

            # Handle implicit multiplication
            expression = self._add_implicit_multiplication(expression)

            # Handle special functions
            expression = self._process_functions(expression)

            # Evaluate
            self.result = eval(expression, {"__builtins__": {}}, {
                "sin": self._sin,
                "cos": self._cos,
                "tan": self._tan,
                "log": math.log10,
                "ln": math.log,
                "sqrt": math.sqrt,
                "pi": math.pi,
                "e": math.e
            })

            # Format result
            if isinstance(self.result, float):
                if self.result.is_integer():
                    self.result = int(self.result)
                else:
                    self.result = round(self.result, 10)

            self.display_text = str(self.result)
            return self.result

        except Exception as e:
            self.display_text = "ERROR"
            return None

    def _add_implicit_multiplication(self, expr):
        # Add * between number and opening parenthesis: 2( -> 2*(
        expr = re.sub(r'(\d)\(', r'\1*(', expr)
        # Add * between closing and opening parenthesis: )( -> )*(
        expr = re.sub(r'\)\(', r')*(', expr)
        # Add * between closing parenthesis and number: )2 -> )*2
        expr = re.sub(r'\)(\d)', r')*\1', expr)
        return expr

    def _process_functions(self, expr):
        # Convert SIN, COS, TAN to lowercase
        expr = re.sub(r'SIN\(', 'sin(', expr)
        expr = re.sub(r'COS\(', 'cos(', expr)
        expr = re.sub(r'TAN\(', 'tan(', expr)
        expr = re.sub(r'LOG\(', 'log(', expr)
        expr = re.sub(r'LN\(', 'ln(', expr)
        return expr

    def _sin(self, x):
        if self.angle_mode == "deg":
            x = math.radians(x)
        return math.sin(x)

    def _cos(self, x):
        if self.angle_mode == "deg":
            x = math.radians(x)
        return math.cos(x)

    def _tan(self, x):
        if self.angle_mode == "deg":
            x = math.radians(x)
        return math.tan(x)

    def square(self, x=None):
        if x is None:
            self.display_text += "²"
        else:
            return x ** 2

    def inverse(self, x=None):
        if x is None:
            self.display_text += "⁻¹"
        else:
            return 1 / x

    def negate(self):
        if self.display_text and self.display_text[0] == "-":
            self.display_text = self.display_text[1:]
        else:
            self.display_text = "-" + self.display_text
