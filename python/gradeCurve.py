import random
import unittest

def classroom():
    students = []
    highestGrade = 0

    for x in range(5):
        student = {}
        student['id'] = random.randint(0,9999999)
        student['grade'] = random.randint(0,100)
        students.append(student)

        if student['grade'] > highestGrade:
            highestGrade = student['grade']

    if highestGrade < 95:
        curve = 95 - highestGrade

        for x in students:
            grade = x['grade'] + curve
            x['curveGrade'] = grade
            if grade >= 90:
                x['grade'] = 'A'
            elif grade >= 80:
                x['grade'] = 'B'
            elif grade >= 70:
                x['grade'] = 'C'
            elif grade >=  60:
                x['grade'] = 'D'
            else:
                x['grade'] = 'F'

    print(students)


class TestGrades(unittest.TestCase):
    
    def Testclassroom(self):
        self.assertAlmostEqual(classroom(),)

classroom()