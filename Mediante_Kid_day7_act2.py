import Addition
import Subtraction
import Multiplication
import Division

def input_number():
    n1 = input("Enter first number:")
    n2 = input("Enter second number:")
    return n1, n2

def gen_result(operation, n1, n2, result):
    if(result != None):
        print(f"\nResult: {n1} {operation} {n2} = {result}")
    print("\n")

while True:
    try:
        operation = str(input("What operation would you like to do?\n[A] Addition\n[B] Subtraction\n[C] Multiplication\n[D] Division\n[Q] Exit Application\n")).lower()
        if(operation == 'a'):
            n1, n2 = input_number()
            gen_result('+', n1, n2, Addition.add(n1, n2))
        elif(operation == 'b'):
            n1, n2 = input_number()
            gen_result('-', n1, n2, Subtraction.subtract(n1, n2))
        elif(operation == 'c'):
            n1, n2 = input_number()
            gen_result('*', n1, n2, Multiplication.multiply(n1, n2))
        elif(operation == 'd'):
            n1, n2 = input_number()
            gen_result('/', n1, n2, Division.divide(n1, n2))
        elif(operation == 'q'):
            print("Application Exited")
            break
        else:
            raise Exception("Operation was not found\n")
    except Exception:
        continue