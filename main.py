import math
# Calculator
from art import logo

# Adding
def add(n1, n2):
  return n1 + n2

# Subtracting
def substract(n1, n2):
  return n1 - n2

# Multiplying
def multiply(n1, n2):
  return n1 * n2

# Dividing
def divide(n1, n2):
  return n1 / n2

# Squareroot
def sqrt(n1, n2):
  return n1 ** (1 / n2)

# Exponent
def exponent(n1, n2):
  return pow(n1, n2)
  
operations = {
  "+": add, 
  "-": substract, 
  "*": multiply, 
  "/": divide,
  "^": sqrt,
  "**": exponent,
}
def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?:\n"))
  should_continue = True
  while should_continue:
    for symbol in operations:
      print(symbol)
      
    operation_symbol = input("Pick an operation symbol:\n(If you use nth root(^) then the second nr type the exponent you want it to take. If you use exponent(**)then the second number will be the power you want to raise the first number in.)\n")
    num2 = float(input("What's the next number?:\n"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2) 
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' if you want to continue calculating with {answer}, or type 'n' if you want to start a new calculation:\n").lower() == "y":
      num1 = answer
    else: 
      should_continue = False
      calculator()
calculator()
