class User:
    first_name = "Имя"
    last_name = "Фамилия"
    student_info = "Имя", "Фамилия"


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_info(self):
        return self.student_info