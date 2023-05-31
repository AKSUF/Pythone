def calculate_grade(scores):
    grades=[]
    for score in scores:
        if score >=90:
            grade="A"
        elif score>=80:
            grade="B"
        elif score>=70:
            grade="C"
        elif score>=60:
            grade="D"
        else:
            grade="F"
        grades.append(grade)
    return grades
student_scores=[75,92,88,67,42,95]
student_grades=calculate_grade(student_scores)

for i in range(len(student_scores)):
    print("Student",i+1,"Score",student_scores[i],"Grade",student_grades[i])
