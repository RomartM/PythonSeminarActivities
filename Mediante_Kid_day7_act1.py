import random

#Init

first_names = ["Tula", "Alvera", "Beverlee", "Thomasina", "Roosevelt", "Neomi", "Collen", "Lila", "Hassan", "Violeta"]
middle_names = ["Barrie", "Wava", "Thu", "Dino", "Avelina", "Rosamaria", "Christia", "Darcel Edmond", "Jarod", "Max"]
last_names = ["Tran", "Long", "Conway", "Davenport", "Wu", "Howell", "Howell", "Velasquez", "Morse", "Garrett"]

generated_names = []

run_program = True

# Define Functions

def generate_names():
    return first_names[random.randint(0, 9)], middle_names[random.randint(0, 9)], last_names[random.randint(0, 9)]

print("Name Generator App")

# Process
while run_program:
    action = str(input("Would you like to generate random name? [y/n]")).lower()
    if(action == "y"):
        fname, mname, lname = generate_names()
        generated_names.append("{} {} {}".format(fname, mname, lname))
        print(f"Congratulations! Your new name is {fname} {mname} {lname}")
    elif(action == "n"):
        count = len(generated_names)
        names = "\n".join(generated_names)
        print("Thank You!")
        print(f"\nNames Generated are the following with a total count of {count}. \n\n{names}")
        break;
    else:
        print("Command not found");
