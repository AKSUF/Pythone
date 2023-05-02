marks=[95,98,97]
print(marks)
print(marks[-1])
print(marks[1])
print(marks[1:3])
marks.append(99)
marks.insert(5,45)
print(marks)
for score in marks:
    print(score)
i=0
while i<len(marks):
    print(marks[i])
    i=i+1
marks.clear()
print(marks)







