def calculate_grade(marks):
    total = sum(marks)
    per = total / 5
    grade = "A" if per >= 80 else "B" if per >= 60 else "C" if per >= 40 else "F"
    return total, per, grade

if __name__ == "__main__":
    marks = [int(input("Enter marks: ")) for i in range(5)]
    total, per, grade = calculate_grade(marks)
    print("Total:", total)
    print("Percentage:", per)
    print("Grade:", grade)
