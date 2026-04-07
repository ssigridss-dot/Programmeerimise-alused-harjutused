from school import School
from student import Student
from course import Course

def test_get_grades():
    course1 = Course("Math")
    student1 = Student("John Smith")
    course1._Course__grades[student1] = 5
    assert course1.get_grades() == [(student1, 5)]


if __name__ == '__main__':
    test_get_grades()
    school = School("Awesome School")
    student1 = Student("John Smith")
    student2 = Student("Mary Lee")

    school.add_student(student1)
    school.add_student(student2)

    # we cannot add one student twice
    school.add_student(student1)

    print(len(school.get_students()))  # 2

    course1 = Course("Math")
    course2 = Course("Physics")
    school.add_course(course1)
    school.add_course(course2)

    # we cannot add one course twice
    school.add_course(course1)

    print(len(school.get_courses()))  # 2

    school.add_student_grade(student1, course1, 4)
    school.add_student_grade(student1, course2, 5)
    school.add_student_grade(student2, course1, 5)

    student3 = Student("Cocoo Turner")

    # cannot add grades to the student who is not in the school
    school.add_student_grade(student3, course1, 5)

    print(len(student3.get_grades()))  # 0

    school.add_student(student3)
    school.add_student_grade(student3, course1, 3)
    school.add_student_grade(student3, course2, 5)

    print(len(student3.get_grades()))  # 2

    print(student3.get_grades())  # [(Math, 3), (Physics, 5)]

    print(course1.get_grades())  # [(John Smith, 4), (Mary Lee, 5), (Cocoo Turner, 3)]

    print("Students ordered by average grade:")
    print(f"{'Student':>15}: avg grade")
    print("-" * 30)
    for student in school.get_students_ordered_by_average_grade():
        print(f"{student.name:>15}: {student.get_average_grade():.2f}")

    print()
    print("Course average grades")
    for course in school.get_courses():
        print(f"{course.name:>10}: {course.get_average_grade():.2f}")