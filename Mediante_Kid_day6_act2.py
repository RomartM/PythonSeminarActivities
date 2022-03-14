import GrossSalary, SalaryDeductions, NetSalary

print("Salary Computation App")

while True:
    action = str(input("\nWould you like to to do? \n[A] Calculate Salary\n[B] Exit Application")).lower()
    if(action == 'a'):
        try:
            name = str(input("\nEnter Name: "))
            rendered_hours = float(input("Enter rendered Hours: "))
            loan = float(input("Enter Loan Amount: "))
            health_insurance = float(input("Enter Health Issurance"))

            gross = GrossSalary.calculate(rendered_hours)
            total_deductions, tax = SalaryDeductions.calculate(gross, loan, health_insurance)
            net_salary = NetSalary.calculate(total_deductions, gross)

            if gross and total_deductions and net_salary:
                print("\nName: {}\nHour: {}\n".format(name, rendered_hours))
                print("Gross Salary: Php {}\n".format(gross))
                print("Tax: Php {}\nLoan: Php {}\nInsurance: Php {}\n".format(tax, loan, health_insurance))
                print("Total Deductions: Php {}\n".format(total_deductions))
                print("Net Salary: Php {}".format(net_salary))

        except Exception:
            print("Something went wrong processing your inputs")
        else:
            continue
    elif(action == 'b'):
        print("Application Exited")
        break
    else:
        continue


