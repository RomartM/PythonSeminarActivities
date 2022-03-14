#Init
records_storage = dict()
line_break = "-----------------------------------------------\n"
run_program = True

# Define Functions
def add_item(key, value):
    records_storage[key] = value

def delete_item(key):
    try:
        del records_storage[key]
    except KeyError:
      print(f"Key '{key}' could not be found")
    except:
      print("Something else went wrong")

def display_data():
    print("Values: ", records_storage)
    print(line_break)

# Run Process
while run_program:
    action = str(input("What would you like to do? \n[A] - Add Data\n[B] - Delete Data\n[C] - End]\n")).lower()
    if(action == 'a'):
        print("\nAdd Data Selected")
        key = str(input("Enter Key: "))
        value = str(input("Enter Value:"))
        add_item(key, value)
        display_data()
    elif(action == 'b'):
        print("\nDelete Data Selected")
        key = str(input("Enter Key: "))
        delete_item(key)
        display_data()
    elif(action == 'c'):
        print("\nTHANK YOU")
        break;
    else:
        print(f"\nThe command '{action}' was not found. Please try again")
        print(line_break)