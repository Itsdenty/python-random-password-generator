import random

# global variables
characters = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
  "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
  "@", "#", "=", "$", "_" ]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
upper = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]
spe = ["@", "#", "=", "$", "_" ]
lower_count = 0
upper_count = 0
numb_count = 0
spe_count = 0
password = ""
password_length = 0

# this function tracks the number of characters generated for each character type
def check_char_type(ind):
  type = ""
  global lower_count
  global upper_count
  global numb_count
  global spe_count
  if ind > 0 and ind < 26:
    upper_count += 1
    type = "upper"
  elif ind > 25 and ind < 52:
    lower_count += 1
    type = "lower"
  elif ind > 51 and ind < 62:
    numb_count += 1
    type = "number"
  else:
    spe_count +=1
    type = "special character"
  return type

# this function generate and return a random index from the character list
def generateIndex(lower, upper):
  rand_index = random.randint(lower, upper)
  rand_char = characters[rand_index]
  check_char_type(rand_index)
  return rand_char

# this function prompts user for password length and validate it as correct
def prompt_for_length():
  global password_length
  try:
    pwd_length = int(input('please enter a number between 8 and 16: '))
    if pwd_length < 8 or pwd_length > 16:
      print("length should be a number between 8 and 16")
      prompt_for_length()
    else:
      password_length = pwd_length
      return pwd_length
  except:
    print("length should be a number between 8 and 16")
    prompt_for_length()

# this is the main function for password generation
def password_generator():
  global password
  global password_length
  prompt_for_length()
  mid_range = password_length / 2
  for i in range(password_length):
    if i < mid_range:
      character = generateIndex(0, 66)
      password += character
    else:
      character = ""
      if upper_count == 0:
        character = generateIndex(0, 25)
      elif lower_count == 0:
        character = generateIndex(26, 51)
      elif numb_count == 0:
        character = generateIndex(52, 61)
      elif spe_count == 0: 
        character = generateIndex(62, 66)
      else:
        character = generateIndex(0, 66)
      password += character

# call the main function
password_generator()

# print the generated password to the screen
print(password)