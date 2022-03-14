
# Define class
class RestaurantReservationApp:

    filename = ""
    adult_per_head = 0
    child_per_head = 0
    exit_lines = "------------------------------ nothing follows ------------------------------"

    def __init__(self, filename='restaurantrecords', adult_per_head = 500, child_per_head = 300):

        print("Restaurant Reservation System\n")

        self.filename = filename + '.txt'
        self.adult_per_head = adult_per_head
        self.child_per_head = child_per_head

        # Create file if does not exist on class init
        if self.isempty(False):
            file_instance = open(self.filename, 'w')
            file_instance.close()

    def parse(self, line_content):
        return line_content.split('|')

    def isempty(self, display_msg=True):
        try:
            file_instance = open(self.filename)
            first_byte = file_instance.read(1)

            if not first_byte:
                if display_msg:
                    print("\nNo records was found")
                return True
            return False
        except Exception:
            file_instance = open(self.filename, 'w')
            file_instance.close()

    def count(self):
        if not self.isempty(False):
            file_instance = open(self.filename)
            lines = 0
            while True:
                line_content = file_instance.readline()
                if len(line_content) > 0:
                    lines = lines + 1
                else:
                    break
            return lines
        return 0

    def add(self, name, date, time, no_adult, no_child):
        file_instance = open(self.filename, "a")
        pk = self.count() + 1 # Increment Data Id
        file_instance.write("{}|{}|{}|{}|{}|{}\n".format(pk, date, time, name, no_adult, no_child))
        file_instance.close()

    def view(self):

        if not self.isempty():
            file_instance = open(self.filename)
            lines = 0
            table_data = [["ID", "Date", "Time", "Name", "Adults", "Children"]]
            while True:
                line_content = file_instance.readline()
                if len(line_content) > 0:
                    lines = lines + 1
                    try:
                        pk, v1, v2, v3, v4, v5 = self.parse(line_content)
                        v5 = v5.rstrip("\n") # Remove new line
                        table_data.append([pk, v1, v2, v3, v4, v5])
                    except ValueError:
                        continue
                else:
                    break
            file_instance.close()
            print('\n'.join([''.join(['{:20}'.format(x) for x in r]) for r in table_data]))

    def delete(self, pk):
        temp = ""
        if not self.isempty():
            file_instance = open(self.filename)
            lines = 0
            is_deleted = False
            while True:
                line_content = file_instance.readline()
                if len(line_content) > 0:
                    lines = lines + 1
                    try:
                        pk_data, v1, v2, v3, v4, v5 = self.parse(line_content)
                        if(pk != int(pk_data)):
                            temp = temp + "{}|{}|{}|{}|{}|{}\n".format(pk_data, v1, v2, v3, v4, v5)
                        else:
                            print("Reservation No ({}) Deleted".format(pk))
                            is_deleted = True
                    except ValueError:
                        continue
                else:
                    break
            if not is_deleted:
                print("No reservation no ({}) was found to be deleted.".format(pk))
            file_instance.close()
            # Overrite Data
            file_instance = open(self.filename, "w")
            file_instance.write(temp)
            file_instance.close()

    def generate(self):
        if not self.isempty():
            file_instance = open(self.filename)
            lines = 0

            total_adults = 0
            total_kids = 0
            grand_total = 0

            table_data = [["ID", "Date", "Time", "Name", "Adults", "Children", "Subtotal"]]

            while True:
                line_content = file_instance.readline()
                if len(line_content) > 0:
                    lines = lines + 1
                    try:
                        pk, v1, v2, v3, v4, v5 = self.parse(line_content)

                        v5 = v5.rstrip("\n") # Remove new line
                        total_adults = total_adults + int(v4)
                        total_kids = total_kids+ int(v5)

                        adult = self.adult_per_head * int(v4)
                        children = self.child_per_head * int(v5)

                        subtotal = adult + children

                        grand_total = grand_total + subtotal
                        table_data.append([pk, v1, v2, v3, v4, v5, subtotal])
                    except ValueError:
                        continue
                else:
                    break

            print('\n'.join([''.join(['{:20}'.format(x) for x in r]) for r in table_data]))
            print("\nTotal Number of Adults: {}".format(total_adults))
            print("Total Number of Kids: {}".format(total_kids))
            print("Grand Total: PHP {}".format(grand_total))
            file_instance.close()

            print(self.exit_lines)

app_instances = RestaurantReservationApp()

def input_qoutes():
    no_adults = 0
    no_children = 0
    try:
        no_adults = int(input("Enter No. of Adults:"))
        no_children = int(input("Enter No. of Children:"))

        if no_adults < 0 or no_children < 0:
            raise Exception("Negative Numbers are not allowed please try again")
    except ValueError:
        print("Invalid Input please try again with numeric value")
        return input_qoutes()
    except Exception as msg:
        print(msg)
        return input_qoutes()
    else:
        return no_adults, no_children

def input_pk():
    pk = 0
    try:
        pk = int(input("Enter the reservation ID:"))
        if pk < 0:
            raise Exception("Negative Numbers are not allowed please try again")
    except ValueError:
        print("Invalid Input please try again with numeric value")
        return input_pk()
    except Exception as msg:
        print(msg)
        return input_pk()
    else:
        return pk

while True:
    action = str(input("\nSystem Menu \n[A] View all Reservations \n[B] Make Reservation \n[C] Delete Reservation \n[D] Generate Report\n[E] Exit?\n")).lower()
    if(action == 'a'):
        app_instances.view()
    elif(action == 'b'):
        name = str(input("\nEnter Name:"))
        date = str(input("Enter Date:"))
        time = str(input("Enter Time:"))

        no_adults, no_children = input_qoutes()
        app_instances.add(name, date, time, no_adults, no_children)
    elif(action == 'c'):
        pk = input_pk()
        app_instances.delete(pk)
    elif(action == 'd'):
        app_instances.generate()
    elif(action == 'e'):
        print("Application Exited")
        break
    else:
        continue