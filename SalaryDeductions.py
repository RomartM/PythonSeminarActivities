def calculate(gross_salary, loan, insurance, vat=12):
    try:
        vat_value = (gross_salary * vat) / 100
        return (loan + insurance + vat_value), vat_value
    except ZeroDivisionError:
        print("Zero division error had occured")
    except ArithmeticError:
        print("Something went wrong about your numbers supplied")
    except OverflowError:
        print("Calculation had exceeded the maximum limit")
    except Exception:
        print("Something went wrong")
    else:
        return False