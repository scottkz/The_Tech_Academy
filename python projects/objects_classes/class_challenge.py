# Parent class
class Student:
    def __init__(self, name, grade, gpa, school, district):
        self.name = "Alex Smith"
        self.grade = 10
        self.gpa = 3.55
        self.school = "Palomena High School"
        self.district = "Orange County School District"

    def get_info(self):
        print(
            "\n{} is a student at {} in the {}. {} is in the {}th grade with a GPA of {}".format(
                self.name,
                self.school,
                self.district,
                self.name,
                self.grade,
                self.gpa,
            )
        )


if __name__ == "__main__":
    student = Student(
        name=Student,
        grade=Student,
        gpa=Student,
        school=Student,
        district=Student,
    )
    student.get_info()
