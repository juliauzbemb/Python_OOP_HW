class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lecturer_rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade_st(self):
        sum_grade = 0
        count = 0
        for grades in self.grades:
            for elements in self.grades[grades]:
                sum_grade += elements
                count += 1
        return round(sum_grade / count, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        return self.get_avg_grade_st() < other.get_avg_grade_st()

    def __str__(self):
        res1 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_avg_grade_st()}\nКурсы ' \
               f'в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
               f'{", ".join(self.finished_courses)} '
        return res1


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        sum_grade = 0
        count = 0
        for grades in self.grades:
            for elements in self.grades[grades]:
                sum_grade += elements
                count += 1
        return round(sum_grade / count, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        return self.get_avg_grade() < other.get_avg_grade()

    def __str__(self):
        res3 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_grade()}'
        return res3


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res4 = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res4


student_1 = Student("John", "Miles", "male")
student_1.courses_in_progress += ["Python", "Git"]
student_1.add_courses("Введение в программирование")
student_2 = Student("Joanna", "Hidings", "female")
student_2.courses_in_progress += ["Python", "Git"]
student_2.add_courses("Введение в программирование")
lecturer_1 = Lecturer("Michael", "Fishman")
lecturer_1.courses_attached += ["Python"]
student_1.lecturer_rate_hw(lecturer_1, "Python", 9)
student_2.lecturer_rate_hw(lecturer_1, "Python", 8)
lecturer_2 = Lecturer("Olga", "Hix")
lecturer_2.courses_attached += ["Git"]
student_1.lecturer_rate_hw(lecturer_2, "Git", 7)
student_2.lecturer_rate_hw(lecturer_2, "Git", 5)
reviewer_1 = Reviewer("Tracy", "Files")
reviewer_1.courses_attached += ["Python"]
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_2, "Python", 10)
reviewer_1.rate_hw(student_2, "Python", 9)
reviewer_2 = Reviewer("Jonathan", "Miles")
reviewer_2.courses_attached += ["Git"]
reviewer_2.rate_hw(student_1, "Git", 9)
reviewer_2.rate_hw(student_1, "Git", 8)
reviewer_2.rate_hw(student_2, "Git", 5)
reviewer_2.rate_hw(student_2, "Git", 9)
student_1.get_avg_grade_st()
student_2.get_avg_grade_st()
lecturer_1.get_avg_grade()
lecturer_2.get_avg_grade()
print(student_1)
print(student_2)
print(student_1.__lt__(student_2))
print(lecturer_1)
print(lecturer_2)
print(lecturer_2.__lt__(lecturer_1))
print(reviewer_1)
print(reviewer_2)

students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]


def av_grade_all_students(students_list, course):
    sum_grade_all_s = 0
    count = 0
    for student in students_list:
        if course in student.courses_in_progress:
            for grades in student.grades[course]:
                sum_grade_all_s += grades
                count += 1
    return round(sum_grade_all_s / count, 2)


def av_grade_all_lecturers(lecturers_list, course):
    sum_grade_all_l = 0
    count = 0
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            for grades in lecturer.grades[course]:
                sum_grade_all_l += grades
                count += 1
    return round(sum_grade_all_l / count, 2)


print(av_grade_all_students(students_list, "Python"))
print(av_grade_all_lecturers(lecturers_list, "Git"))
