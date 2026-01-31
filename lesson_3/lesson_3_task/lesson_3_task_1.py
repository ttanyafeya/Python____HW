#Создайте в классе три метода, которые печатают:
# имя,
# фамилию,
# имя и фамилию.

from user import User

student = User("Имя", "Фамилия")


print(student.get_first_name())
print(student.get_last_name())
print(student.get_student_info())


