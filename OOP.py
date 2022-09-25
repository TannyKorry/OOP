class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rating(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and grade in range(1, 11):
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def collecting_all_grades(self):
        """The function generates a complete list of grades of the student, excluding the course"""
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        return grades_list

    def __str__(self):
        res = f'Студент \n' \
              f'     Имя: {self.name}\n' \
              f'     Фамилия: {self.surname}\n' \
              f'     Средняя оценка за домашние задания: {round(sum(self.collecting_all_grades()) / len(self.collecting_all_grades()), 1)}\n' \
              f'     Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'     Завершенные курсы: {", ".join(self.finished_courses)}' \
              f'\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Students):
            print('Not a Students!')
            return
        return sum(self.collecting_all_grades()) / len(self.collecting_all_grades()) < \
            sum(other.collecting_all_grades()) / len(other.collecting_all_grades())


class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentors):
    grades = {}

    def collecting_all_grades(self):
        """The function generates a complete list of grades of the lecturer, excluding the course"""
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        return grades_list

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return sum(self.collecting_all_grades()) / len(self.collecting_all_grades()) < \
            sum(other.collecting_all_grades()) / len(other.collecting_all_grades())

    def __str__(self):
        res = f'Лектор \n' \
              f'     Имя: {self.name}\n' \
              f'     Фамилия: {self.surname}\n' \
              f'     Средняя оценка за лекции: {round(sum(self.collecting_all_grades()) / len(self.collecting_all_grades()), 1)}' \
              f'\n'
        return res


class Reviewer(Mentors):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Students) and course in student.courses_in_progress and grade in range(1, 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Проверяющий \n' \
              f'     Имя: {self.name}\n' \
              f'     Фамилия: {self.surname}' \
              f'\n'
        return res


best_student = Students('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

other_student = Students('Kate', 'Thomson', 'your_gender')
other_student.finished_courses += ['Введение в программирование']
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']

some_reviewer = Reviewer('Bobby', 'Fox')
other_reviewer = Reviewer('Layhem', 'Birch')

some_lecturer = Lecturer('Billy', 'Smith')
other_lecturer = Lecturer('Paul', 'Stone')

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 10)
other_reviewer.rate_hw(best_student, 'Git', 8)

some_reviewer.rate_hw(other_student, 'Git', 8)
some_reviewer.rate_hw(other_student, 'Git', 10)
some_reviewer.rate_hw(other_student, 'Git', 7)

other_reviewer.rate_hw(other_student, 'Python', 8)
other_reviewer.rate_hw(other_student, 'Python', 3)
other_reviewer.rate_hw(other_student, 'Python', 7)

best_student.rating(some_lecturer, 'Python', 10)
best_student.rating(some_lecturer, 'Git', 10)
other_student.rating(some_lecturer, 'Python', 5)
best_student.rating(other_lecturer, 'Git', 7)
other_student.rating(other_lecturer, 'Python', 8)

print(some_lecturer)
print(other_lecturer)
print(some_reviewer)
print(other_reviewer)
print(best_student)
print(other_student)
print(best_student > other_student)
print(some_lecturer < other_lecturer)
