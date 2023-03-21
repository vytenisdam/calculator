from art import logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def add(x, y):
  """Adding numbers"""
  return x + y
  
def subtract(x, y):
  """Subtracts numbers"""
  return x - y
  
def multiply(x, y):
  """Multiplies numbers"""
  return x * y
  
def divide(x, y):
  """Divides numbers"""
  return x / y
  
operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
    print(logo)
    x = float(input("What's the first number?\n"))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick the operation from the line above?\n")
    y = float(input("What's the second number?\n"))
    calculation_function = operations[operation_symbol]
    first_answer = float(calculation_function(x, y))
    print(f"{x} {operation_symbol} {y} = {first_answer}")

    continue_process = True

    decision = input(f"Would you like to continue the process with the number - {first_answer}? type 'y' to continue, 'n' or 'Bye' to turn the calculator off.\n")
    continue_process = True
    while continue_process:
        if decision == 'n':
            continue_process = False
            cls()
            calculator()
        elif decision == 'y':
            operation_symbol = input("Pick another operation: ")
            z = float(input("What's the next number?\n"))
            calculation_function = operations[operation_symbol]
            second_answer = float(calculation_function(first_answer, z))
            print(f"{first_answer} {operation_symbol} {z} = {second_answer}")
            first_answer = second_answer
            decision = input(f"Would you like to continue the process with the number - {second_answer}? type y or n.\n")
        else:
            continue_process = False
            cls()
            print('See ya later!')
        
calculator()