#Define Class

class Employee:

    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number

    def display(self):
        print("Employee Details: \nName:{}\nEmail:{}\nMobile Number:{}\n".format(self.name, self.email, self.mobile_number))

# Init Class

employee_1 = Employee("Jhon Doe", "webmasters@mail.com", "09123456789")
employee_2 = Employee("Alexa Duett", "alexas@mail.com", "0987654321")


# Display Details

employee_1.display()
employee_2.display()