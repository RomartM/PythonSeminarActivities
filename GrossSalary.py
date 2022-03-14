def calculate(rendered_hours, rate_per_hour=500):
    try:
        return rate_per_hour * rendered_hours
    except ArithmeticError:
        print("Something went wrong about your numbers supplied")
    except OverflowError:
        print("Calculation had exceeded the maximum limit")
    except Exception:
        print("Something went wrong")
    else:
        return False