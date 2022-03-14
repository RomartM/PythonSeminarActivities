initial_value = int(input("Enter Initial Value: "))

first_init_val = ( 1 / initial_value ) + 1
second_init_val = ( 1 / first_init_val ) + 1
third_init_val = ( 1 / second_init_val ) + 1

print(f"Initial Value: {initial_value}")
print(f"First Value: {first_init_val}")
print(f"Second Value: {second_init_val}")
print(f"Third Value: {third_init_val}")