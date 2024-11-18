from typing import Tuple

student: tuple[str, int, str] = ("Richard", 29, "male")
print(student.count("Richard"))
print(student.index("male"))

for i in student :
    print(i)
if "Richard" in student :
    print("Richard is a student")