def calculate_grade_average(name, math, english, science):
    grades = [math, english, science]
    average = round(sum(grades) / len(grades), 2)
    print(f"{name}'s grade (Math={math}, Science={science}, English={english}) and the average is {average}")

calculate_grade_average("Jane", 91.5, 87, 95)
calculate_grade_average("Mark", 80, 84, 88)
calculate_grade_average("Kevin", 95, 94, 96)