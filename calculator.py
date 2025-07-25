# calculator.py

# defining the functions for all the actions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# defining the statements
print("🔢 Simple Calculator in Python")
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")


# Applying the code
while True:

  #try to check for the error
  try:  
    choice = int(input("Enter choice (1/2/3/4): "))
    if choice < 1 or choice > 4:
      raise ValueError # value error is defined below and it can be called
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue  # this continue will start the program from the first

  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  if choice == 1:
    print(f"{num1} + {num2} = {add(num1, num2)}")
  elif choice == 2:
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
  elif choice == 3:
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
  elif choice == 4:
    if num2 == 0:
      print("Error! Division by zero.")
    else:
      print(f"{num1} / {num2} = {divide(num1, num2)}")
  
  print("Want to continue? yes/no? \n")
  choice = input()
  if choice.lower() == "no":
    print("Thank you for using our Calculator")
    break





