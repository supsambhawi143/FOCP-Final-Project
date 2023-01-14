#Task3final
#Program to read and write output in a text file
import sys
import random

#Function to generate email
def generate_email(name, id):
    """This program splits first name initials into parts and concatenate with surname, 
    random digits and remaining domain to form an email"""
    name_parts = name.split(", ")
    surname = name_parts[0]
    forenames = name_parts[1]

    surname = "".join([x for x in surname if x.isalpha()])

    initials = ".".join([x[0] for x in forenames.split() if x[0].isalpha()])

    #for loop to print the random digits
    ran_digits = "".join([str(random.randint(0, 9)) for _ in range(4)])

    # concatenate to form an email
    email = initials + "." + surname + ran_digits + "@poppleton.ac.uk"
    return email.lower() 

    # Checks if the file name is provided with a command line argument or not
if (len(sys.argv)) < 2:
  print("Error: Missing command-line argument.")
  sys.exit()

    #try to open the file
try:
    with open(sys.argv[1], "r") as input_file, open("emails.txt", "w") as output_file:
        # Reads the file and splits into id and name
        for line in input_file:
            id = line.split()[0]
            name = line[1:]
            email = generate_email(name, id)
            output_file.write(f"{id} {email}\n")
            
#Prints the output if file doesn't exist 
except IOError:
    print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")