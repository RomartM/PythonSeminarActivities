# Init

template_payslip = ("\n===============PAYSLIP===============\n"
                    "\n========EMPLOYEE INFORMATION=========\n"
                    "Employee Name:     {employee_name}\n"
                    "Rendered Hours:    {rendered_hours}\n"
                    "Rate per Hour:     {rate_per_hour}\n"
                    "Gross Salary:      {gross_salary}\n"
                    "\n=============DEDUCTIONS==============\n"
                    "SSS:               {sss}\n"
                    "PhilHealth:        {philhealth}\n"
                    "Other Loan:        {other_loan}\n"
                    "Tax:               {tax}\n"
                    "Total Deductions:  {total_deductions}\n\n"
                    "Net Salary:        PHP {net_salary}"
                    )

tax = 500.0
rate_per_hour = 800

# Input

employee_name = input("Employee Name: ")
number_of_hours = float(input("Enter number of hours: "))
sss_contribution = float(input("SSS contribution: "))
phil_health = float(input("Phil health: "))
housing_loan = float(input("Housing loan: "))

# Process

gross_salary = number_of_hours * rate_per_hour
total_deductions = sss_contribution + phil_health + housing_loan + tax
net_salary = gross_salary - total_deductions

# Template Prefilling

output = template_payslip.replace("{employee_name}", employee_name, 1)
output = output.replace("{rendered_hours}", "%.f" % number_of_hours, 1)
output = output.replace("{rate_per_hour}", "%.f" % rate_per_hour, 1)
output = output.replace("{gross_salary}", "%.1f" % gross_salary, 1)
output = output.replace("{sss}", "%.f" % sss_contribution, 1)
output = output.replace("{philhealth}", "%.f" % phil_health, 1)
output = output.replace("{other_loan}", "%.f" % housing_loan, 1)
output = output.replace("{tax}", "%.1f" % tax, 1)
output = output.replace("{total_deductions}", "%.1f" % total_deductions, 1)
output = output.replace("{net_salary}", "%.1f" % net_salary, 1)

# Output

print(output)
