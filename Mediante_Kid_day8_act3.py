#Define Class

class Student:

    __name = ""
    __math = 0
    __science = 0
    __english = 0
    __grade_average = 0
    __grade_status = ""
    __status = True

    def __init__(self, name, math, science, english):
        try:
            self.__name = str(name)
            self.__math = float(math)
            self.__science = float(science)
            self.__english = float(english)
        except Exception:
            self.__status = False
            print("Something went wrong.")

    def calculate_average(self):
        try:
            grade_sum = self.__math + self.__science + self.__english
            self.__grade_average = grade_sum / 3
            self.__grade_status = ""

            if(self.__grade_average >= 75):
                self.__grade_status = "Passed"
            else:
                self.__grade_status = "Failed"
        except ZeroDivisionError:
            print("Zero division error had occured")
            self.__status = False
        except ArithmeticError:
            print("Something went wrong about your numbers supplied")
            self.__status = False
        except OverflowError:
            print("Calculation had exceeded the maximum limit")
            self.__status = False
        except Exception:
            print("Something went wrong")
            self.__status = False


    def display(self):
        self.calculate_average()
        if self.__status:
            print("\nName: {}".format(self.__name))
            print("Math: {}\nScience: {}\nEnglish: {}".format(self.__math, self.__science, self.__english))
            print("Average: {} ({})".format(self.__grade_average, self.__grade_status))
        else:
            print("Unable to calculate")



while True:
    action = str(input("\nWould you like to to do \n[A] Calculate Grade\n[B] Exit Application?")).lower()
    if(action == 'a'):
        name = input("Enter Name:")
        math = input("Enter Math Grade:")
        science = input("Enter Science Grade:")
        english = input("Enter English Grade")

        student_instance = Student(name, math, science, english)
        student_instance.display()
    elif(action == 'b'):
        print("Application Exited")
        break
    else:
        continue
