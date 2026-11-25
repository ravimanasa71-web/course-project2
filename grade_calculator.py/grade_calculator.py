
# grade_calculator.py

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def main():
    marks = float(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
    else:
        grade = calculate_grade(marks)
        print("Your Grade is:", grade)


if __name__ == "__main__":
    main()

