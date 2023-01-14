#Task1final
#Program to generate passwords of random words
import random

# Constant for the lists
COLORS = ['yellow', 'purple', 'pink', 'black', 'red', 'brown']
ANIMALS = ['dog', 'horse', 'rabbit', 'sheep', 'lion', 'monkey']
HOMES = ['den', 'fold', 'stable', 'tree', 'burrow', 'kennel']

def generate_password():
  """This program generates a password by choosing 
  random values from the lists"""    
  # Choose a random word from each list
  colors = random.choice(COLORS)
  animals = random.choice(ANIMALS)
  homes = random.choice(HOMES)

  # Returns the password by concatenating the words
  return colors + animals + homes

 # Main function
def main():
    
  #displays the following written inside parentheses 
  print("Password Generator")
  print("==================")

  try:
    #prompt user to enter the number of passwords
    password_count = int(input("Enter the number of passwords needed: "))
  except:
    print("Please enter a number.")
    exit()

  # Check that the number is between 1 and 24 
  if password_count < 1 or password_count > 24:
    print("Please enter a value between 1 and 24.")
    return

  # Displays the passwords
  for i in range(password_count):
    password = generate_password()
    print(f"{i + 1} --> {password}")

# Run the main function
if __name__ == "__main__":
  main()