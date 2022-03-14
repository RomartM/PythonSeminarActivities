def divide(n1, n2):
    try:
        return float(n1) / float(n2)
    except ZeroDivisionError:
        print(f"{n1} is not divisible by {n2}")
    except ArithmeticError:
        print("Something went wrong about your numbers supplied")
    except OverflowError:
        print("Calculation had exceeded the maximum limit")
    except Exception:
        print("Something went wrong")
    else:
        return None