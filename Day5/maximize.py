student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68]

max_score = max(student_score)
print(max_score)

maximum_score = 0
for score in student_score:
    if score > maximum_score:
        maximum_score = score
print(maximum_score)

