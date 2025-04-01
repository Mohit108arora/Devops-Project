print ('hello world')
 
# num = int(input("Enter your number: "))
# lim = int(input("Enter limit of table: "))
# for b in range(1, lim+1):
#     print('{:2} * {:2} = {:2}'.format(num, b, num*b))

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: Division by zero is not allowed."
#     else:
#         return x / y

# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     while True:
#         choice = input("Enter choice(1/2/3/4): ")
#         if choice in ('1', '2', '3', '4'):
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             if choice == '1':
#                 print(num1, "+", num2, "=", add(num1, num2))
#             elif choice == '2':
#                 print(num1, "-", num2, "=", subtract(num1, num2))
#             elif choice == '3':
#                 print(num1, "*", num2, "=", multiply(num1, num2))
#             elif choice == '4':
#                 print(num1, "/", num2, "=", divide(num1, num2))
#             next_calculation = input("Do you want to continue calculation (yes/no): ")
#             if next_calculation == "no":
#                 break
#         else:
#             print("Invalid input")

# calculator()

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x400")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=20)
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 2),
            ("=", 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, text):
        if text == "=":
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()