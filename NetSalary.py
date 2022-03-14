def calculate(deductions, gross_salary):
    try:
        return gross_salary - deductions
    except ArithmeticError:
        print("Something went wrong about your numbers supplied")
    except OverflowError:
        print("Calculation had exceeded the maximum limit")
    except Exception:
        print("Something went wrong")
    else:
        return False
