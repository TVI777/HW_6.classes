def calc_average(self):
    temps = []
    for temp in self.values():
        temps += temp
        average = round(sum(temps) / len(temps), 1)
    return average

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.average_stud < other.average_stud

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.average_stud > other.average_stud

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.average_stud == other.average_stud

    def __str__(self):
         return  (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: '
                  f'{average_stud}\nКурсы в процессе обучени: {", ".join(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {", ".join(self.finished_courses)}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.average_lec < other.average_lec
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.average_lec > other.average_lec

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.average_lec == other.average_lec


    def __str__(self):
         return  f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_lec} '


class Reviewer(Mentor):
    def __init__(self, name, surname):
         super().__init__(name, surname)

    def __str__(self):
         return  f'Имя: {self.name}\nФамилия: {self.surname}'




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Git']
best_lecturer1 = Lecturer('Петр', 'Петров')
best_lecturer1.courses_attached += ['Python']
best_lecturer2 = Lecturer('Сидор', 'Сидоров')
best_lecturer2.courses_attached += ['Введение в программирование']


cool_reviewer = Reviewer('Петр', 'Петров')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 2)
best_student.rate_hw(best_lecturer,'Git', 8)
best_student.rate_hw(best_lecturer,'Git', 9)
best_student.rate_hw(best_lecturer,'Git', 3)

average_lec = calc_average(best_lecturer.grades)
average_stud = calc_average(best_student.grades)

# print(best_student.name, best_student.grades)
# print(best_lecturer.name, best_lecturer.surname, best_lecturer.grades)
print(cool_reviewer)
print()
print(best_lecturer)
print()
print(best_student)