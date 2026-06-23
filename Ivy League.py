students_information={"name":"wassim","age":38,"university":"codegym"}

if "MIT" in students_information.values():
    print("MIT is precence")
else:
    print("MIF is not precence")

found=set(students_information.values())

if "Harved" in found:
    print("Harved is precence")
else:
    print("Harved is not precence")
check=25
if any(value==check for value in students_information.values()):
    print(f"The value {check} is precence")
else:
    print(f"The value {check}is no precence")

