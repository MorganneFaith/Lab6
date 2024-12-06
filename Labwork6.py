import pickle


class CourseGrades:
    def __init__(self):
        self.course_name = ""
        self.stu_id = []
        self.stu_grades = []

    def create(self):
        self.course_name = input("Enter course name: ")
        for i in range(5):
            self.stu_id.append(input("Enter student id: "))
        for i in range(5):
            self.stu_grades.append(input("Enter grade: "))


c1 = CourseGrades()
c1.create()

c2 = CourseGrades()
c2.create()

c3 = CourseGrades()
c3.create()

c4 = CourseGrades()
c4.create()


f = open('grades_info.dat', 'ab')
pickle.dump(c1, f)
pickle.dump(c2, f)
pickle.dump(c3, f)
pickle.dump(c4, f)
f.close()

f = open('grades_info.dat', 'rb')

while 1:
    try:
        data = pickle.load(f)
        print(data.course_name)
        print(data.stu_id)
        print(data.stu_grades)

    except EOFError:
        break
f.close()






