"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
  user_input = input("Enter in your equation --> ")
  tokens = user_input.split(' ')

# defines variables
  user_command = tokens[0].lower()
  
  if user_command == 'q':
      print("You are done")
      break
  
  elif len(tokens) == 2:
      num1 = float(tokens[1])
      num2 = 0
  
  elif len(tokens) >= 3:
      num1 = float(tokens[1])
      num2 = float(tokens[2])
  
  else:
      print('aahhhh')
  

# executes functions

  if user_command == 'pow':
      print(power(num1, num2))

  elif user_command == '+':
      print(add(num1, num2))

  elif user_command == '-':
      print(subtract(num1, num2))

  elif user_command == '*':
      print(multiply(num1, num2))  

  elif user_command == '/':
      print(divide(num1, num2))

  elif user_command == 'square':
      print(square(num1))  

  elif user_command == 'cube':
      print(cube(num1))

  elif user_command == 'mod' or user_command == '%':
      print(mod(num1, num2))  

  else:
      print("Wrong input!")