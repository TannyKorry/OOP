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

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {round(sum(*self.grades.values()) / len(*self.grades.values()), 1)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Students):
            print('Not a Students!')
            return
        return sum(*self.grades.values()) / len(*self.grades.values()) < \
            sum(*other.grades.values()) / len(*other.grades.values())


class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentors):
    grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {round(sum(*self.grades.values()) / len(*self.grades.values()), 1)}'
        return res


class Reviewer(Mentors):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Students) and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Students('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

other_student = Students('Kate', 'Thomson', 'your_gender')
other_student.finished_courses += ['Введение в программирование']
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']

cool_mentor = Mentors('Some', 'Buddy')

some_reviewer = Reviewer('Bobby', 'Fox')
some_lecturer = Lecturer('Billy', 'Smith')

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)

some_reviewer.rate_hw(other_student, 'Python', 8)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 7)

best_student.rating(some_lecturer, 'Python', 10)
best_student.rating(some_lecturer, 'Python', 10)
best_student.rating(some_lecturer, 'Python', 11)

# print(best_student.grades)
# print(cool_lecturer.grades)
print(some_lecturer)
# print(some_reviewer)
print(best_student)
print(other_student)
print(best_student > other_student)
