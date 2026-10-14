# Lab 01 - Python Fundamentals
# Problems 1 to 4 from the lab manual

# Problem 1: Basic arithmetic
print("Problem 1: Basic Arithmetic")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)

if number2 != 0:
    print("Quotient:", number1 / number2)
else:
    print("Quotient cannot be calculated because the second number is zero.")

# Problem 2: Student profile
print("\nProblem 2: Student Profile")
name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
age = int(input("Enter your age: "))
department = input("Enter your department: ")
cgpa = float(input("Enter your CGPA: "))

print("\nStudent Profile")
print("Name:", name)
print("Student ID:", student_id)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)

# Problem 3: Celsius to Fahrenheit and Kelvin
print("\nProblem 3: Temperature Conversion")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", round(fahrenheit, 2))
print("Kelvin:", round(kelvin, 2))

# Problem 4: Course marks
print("\nProblem 4: Course Marks")
student_name = input("Enter the student's name: ")
marks = []

for course in range(1, 6):
    mark = float(input("Enter mark for course " + str(course) + ": "))
    marks.append(mark)

total = 0
passed = 0
highest = marks[0]
lowest = marks[0]

for mark in marks:
    total = total + mark

    if mark >= 50:
        passed = passed + 1

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / len(marks)

print("\nResults for", student_name)
print("Marks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Courses passed:", passed)
