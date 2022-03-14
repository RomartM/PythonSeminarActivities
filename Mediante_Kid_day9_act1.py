
# Define class
class RecordKeepingApp:

    filename = ""
    separator = "---------"

    def __init__(self, filename='filestore'):

        print("Record Keeping App\n")

        self.filename = filename + '.txt'
        # Create file if does not exist on class init
        if self.isempty():
            file_instance = open(self.filename, 'w')
            file_instance.close()

    def parse(self, line_content):
        return line_content.split('|')

    def isempty(self):
        try:
            file_instance = open(self.filename)
            first_byte = file_instance.read(1)

            if not first_byte:
                print("\nNo records was found")
                return True
            return False
        except Exception:
            file_instance = open(self.filename, 'w')
            file_instance.close()

    def add(self, name, email, address):
        file_instance = open(self.filename, "a")
        file_instance.write("{}|{}|{}\n".format(name, email, address))
        file_instance.close()

    def view(self):

        if not self.isempty():
            file_instance = open(self.filename)
            lines = 0
            while True:
                line_content = file_instance.readline()
                if len(line_content) > 0:
                    lines = lines + 1
                    v1, v2, v3 = self.parse(line_content)
                    print("\nName: {}\nEmail: {}\nAddress: {}".format(v1, v2, v3))
                    print(self.separator)
                else:
                    break

    def clear(self):
        file_instance = open(self.filename, "w")
        file_instance.close()
        self.isempty()

app_instances = RecordKeepingApp()

while True:
    action = str(input("\nWould you like to to do \n[A] Add Record \n[B] View Records \n[C] Clear All Records \n[D] Exit?\n")).lower()
    if(action == 'a'):
        name = str(input("\nEnter Name:"))
        email = str(input("Enter Email:"))
        address = str(input("Enter Address:\n"))

        app_instances.add(name, email, address)
    elif(action == 'b'):
        app_instances.view()
    elif(action == 'c'):
        app_instances.clear()
    elif(action == 'd'):
        print("Application Exited")
        break
    else:
        continue