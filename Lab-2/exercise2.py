# Lab 02 - Collections,Loops and Functions

# Problem 1:
print("Problem 1: Course Marks")
course_marks = [75, 82, 68, 91, 47]
total_marks = 0
passed_courses = 0
highest_mark = course_marks[0]
lowest_mark = course_marks[0]

for mark in course_marks:
    total_marks = total_marks + mark

    if mark >= 50:
        passed_courses = passed_courses + 1

    if mark > highest_mark:
        highest_mark = mark

    if mark < lowest_mark:
        lowest_mark = mark

average_mark = total_marks / len(course_marks)
print("Marks:", course_marks)
print("Total:", total_marks)
print("Average:", round(average_mark, 2))
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)
print("Passed courses:", passed_courses)

# Problem 2:
print("\nProblem 2: Weekend Temperatures")
temperatures = (30.5, 31.0, 29.5, 32.0, 33.2, 31.8)
reading_number = 1
highest_temperature = temperatures[0]
lowest_temperature = temperatures[0]

for temperature in temperatures:
    if reading_number <= 3:
        day = "Saturday"
        day_reading = reading_number
    else:
        day = "Sunday"
        day_reading = reading_number - 3

    print(day, "reading", day_reading, ":", temperature, "C")

    if temperature > highest_temperature:
        highest_temperature = temperature

    if temperature < lowest_temperature:
        lowest_temperature = temperature

    reading_number = reading_number + 1

print("Highest temperature:", highest_temperature, "C")
print("Lowest temperature:", lowest_temperature, "C")

# Problem 3:
print("\nProblem 3: Word Analyzer")
text = input("Enter a word or short sentence: ")
vowel_count = 0
space_count = 0

for character in text:
    if character.lower() in "aeiou":
        vowel_count = vowel_count + 1

    if character == " ":
        space_count = space_count + 1

print("Number of characters:", len(text))
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)

# Problem 4:
def calculate_grade(marks):
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

print("\nProblem 4: Grade Calculator")
student_marks = [85, 72, 66, 55, 41]
student_total = 0

for mark in student_marks:
    student_total = student_total + mark

student_average = student_total / len(student_marks)
print("Marks:", student_marks)
print("Average:", round(student_average, 2))
print("Grade:", calculate_grade(student_marks))

#Product records
products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

# Problem 5:
def apply_discount(total):
    if total >= 2000:
        total = total - (total * 0.10)
    return total

print("\nProblem 5: Shopping Cart Processor")
cart_total = 0

for product in products:
    line_total = product["price"] * product["quantity"]
    print(product["name"], "-", product["quantity"], "x", product["price"], "=", line_total)
    cart_total = cart_total + line_total

final_total = apply_discount(cart_total)
print("Total before discount:", cart_total)
print("Total after discount (if applicable):", round(final_total, 2))

# Problem 6:
print("\nProblem 6: Countdown")
number = int(input("Enter a non-negative integer: "))

while number < 0:
    print("Please enter a non-negative integer.")
    number = int(input("Enter a non-negative integer: "))

while number >= 0:
    print(number)
    number = number - 1

# Problem 7:
print("\nProblem 7: Student Record Analyzer")
students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

passed_students = 0
total_student_marks = 0
top_student_name = students[0]["name"]
top_student_mark = students[0]["marks"]

for student in students:
    print(student["name"], "- Marks:", student["marks"])
    total_student_marks = total_student_marks + student["marks"]

    if student["marks"] >= 50:
        passed_students = passed_students + 1

    if student["marks"] > top_student_mark:
        top_student_mark = student["marks"]
        top_student_name = student["name"]

class_average = total_student_marks / len(students)
print("Students passed:", passed_students)
print("Class average:", round(class_average, 2))
print("Highest mark:", top_student_mark, "by", top_student_name)

# Problem 8:
print("\nProblem 8: Product Inventory Summary")
inventory_total = 0
highest_line_total = 0
highest_value_product = ""

for product in products:
    line_total = product["price"] * product["quantity"]
    print(product["name"], "line total:", line_total)
    inventory_total = inventory_total + line_total

    if line_total > highest_line_total:
        highest_line_total = line_total
        highest_value_product = product["name"]

print("Total inventory value:", inventory_total)
print("Highest line total:", highest_value_product, "-", highest_line_total)
