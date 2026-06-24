student_inf={"name":"wassim","age":38}
print(student_inf)
student_inf["university"]="codegym"
print(student_inf)

if "city" not in student_inf:
    student_inf["city"]="aleppo"
print(student_inf)
new_element={"birth year":1987,"current year":2026}
student_inf.update(new_element)
print(student_inf)
