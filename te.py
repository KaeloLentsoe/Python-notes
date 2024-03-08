exam_score = float(input("Enter your exam score: "))

if 90 <= exam_score <= 100:
    grade = "A"
elif 80 <= exam_score < 90:
    grade = "B"
elif 70 <= exam_score < 80:
    grade = "C"
elif 60 <= exam_score < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)



