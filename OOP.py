class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rating(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and grade <= 10:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


best_student = Students('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentors('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']


class Lecturer(Mentors):
    grades = {}


class Reviewer(Mentors):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Students) and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


cool_reviewer = Reviewer('Bobby', 'Fox')
cool_lecturer = Lecturer('Billy', 'Smith')

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rating(cool_lecturer, 'Python', 10)
best_student.rating(cool_lecturer, 'Python', 10)
best_student.rating(cool_lecturer, 'Python', 11)

print(best_student.grades)
print(cool_lecturer.grades)