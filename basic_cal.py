def calculate(num1, num2, operator):
  """
  Performs a basic calculation based on the provided operator.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The mathematical operator (+, -, *, /).

  Returns:
      The result of the calculation.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
      return None
    else:
      return num1 / num2
  else:
    print("Error: Invalid operator")
    return None

while True:
  # Get user input for numbers and operator
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operation (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue

  # Perform the calculation and display the result
  result = calculate(num1, num2, operator)
  if result is not None:
    print(f"{num1} {operator} {num2} = {result}")

  # Ask the user if they want to continue
  user_choice = input("Do you want to perform another calculation? (y/n): ")
  if user_choice.lower() != 'y':
    break

print("Thank you for using the calculator!")