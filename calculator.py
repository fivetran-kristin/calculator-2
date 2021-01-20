"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
  user_input = input("Enter in your equation -->")
  tokens = user_input.split(' ')

  user_command = tokens[0].lower()
  
  if user_command == 'q':
      print("You are done")
      break
  
  num1 = float(tokens[1])
  num2 = float(tokens[2])
  
  if user_command == 'pow':
      print(power(num1, num2))

  elif user_command == '+':
      print(add(num1, num2))  

# > + 1 2
# 3.0
# > - 10 5
# 5.0
# > * 2 3
# 6.0
# > / 7 2
# 3.5
# > square 2
# 4.0
# > cube 3
# 27.0
# > pow 2 5
# 32.0
# > mod 10 3
# 1.0
# > q