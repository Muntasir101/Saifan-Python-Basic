grade1 = float(input("Enter the grade of first subject: "))
grade2 = float(input("Enter the grade of second subject: "))
grade3 = float(input("Enter the grade of third subject: "))

total_grades = grade1 + grade2 + grade3
average_grade = total_grades / 3

# classify student's performance
if average_grade >= 90:
    performance = "Excellent"
elif average_grade >= 70:
    performance = "Good"
elif average_grade >= 50:
    performance = "Average"
else:
    performance = "Poor"

print(f"Total Grades: %s" % total_grades)
print(f"Average Grades: %s" % average_grade)
print(f"Performance : %s" % performance)