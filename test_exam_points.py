import unittest
from specialization import Specialization
from exam_points import ExamPoints
from exam import Exam
from student import Student
from subject import Subject
from group import Group
from institute import Institute
from datetime import date


class TestClassExamPoints(unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, specialization)
        subject = Subject("1", "2", 3, 4, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович", group)
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 12.3, exam)
        self.assertEqual(student, examPoints.student)
        self.assertEqual(65.4, examPoints.inPoints)
        self.assertEqual(12.3, examPoints.examPoints)


class TestAddExamResult(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specialization1 = Specialization("ФИИТ")
        cls.specialization2 = Specialization("ИВТ")
        cls.group1 = Group("М-ФИИТ-21", 2021, cls.specialization1)
        cls.group2 = Group("М-ИВТ-21", 2021, cls.specialization2)
        cls.subject1 = Subject("Б1.Б.22", "Основы программирования",
                               1, 144, cls.specialization1)
        cls.subject2 = Subject("Б1.Б.24", "Математический анализ",
                               1, 144, cls.specialization2)
        cls.examDate1 = date(2022, 3, 25)
        cls.examDate2 = date(2022, 5, 25)
        cls.exam1 = Exam(cls.subject1, cls.examDate1, 2022,
                         "Иванов Иван Иванович", cls.group1)
        cls.exam2 = Exam(cls.subject2, cls.examDate2, 2022,
                         "Петров Петр Петрович", cls.group2)

    def test_1(self):  # CORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 12.3, self.exam1)
        institute = Institute()
        institute.add_exam_result(examPoints)
        self.assertEqual(len(institute.exam_results), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(None)  # exam points is null
        self.assertTrue(
            'Exam points must not be null' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_3(self):  # CORRECT
        student1 = Student("Федоров Байытаан Павлович", 123456)
        student2 = Student("Иванов Иван Иванович", 456789)
        examPoints1 = ExamPoints(student1, 65.4, 12.3, self.exam1)
        examPoints2 = ExamPoints(student2, 45.6, 23.1, self.exam2)
        institute = Institute()
        institute.add_exam_result(examPoints1)
        institute.add_exam_result(examPoints2)
        self.assertEqual(len(institute.exam_results), 2)

    def test_4(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 12.3, self.exam1)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
            institute.add_exam_result(examPoints)  # re-entry
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 1)

    def test_5(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(
            1, 65.4, 12.3, self.exam1)  # student type error
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue(
            'Wrong type: must be Student' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_6(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        # inpoints is not float
        examPoints = ExamPoints(student, 65, 12.3, self.exam1)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue('Wrong type: must be float' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_7(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        # exampoints is not float
        examPoints = ExamPoints(student, 65.4, 12, self.exam1)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue('Wrong type: must be float' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_8(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)  # inpoints > 70
        examPoints = ExamPoints(student, 85.4, 12.3, self.exam1)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue(
            'In points must be lower than 70' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_9(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 42.3,
                                self.exam1)  # exampoints > 30
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue(
            'Exam points must be lower than 30' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)


class TestGetExamResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specialization1 = Specialization("ФИИТ")
        cls.specialization2 = Specialization("ИВТ")
        cls.group1 = Group("М-ФИИТ-21", 2021, cls.specialization1)
        cls.group2 = Group("М-ИВТ-21", 2021, cls.specialization2)
        cls.student1 = Student("Федоров Байытаан Павлович", 123456)
        cls.student2 = Student("Иванов Иван Иванович", 456789)
        cls.subject1 = Subject("Б1.Б.22", "Основы программирования",
                               1, 144, cls.specialization1)
        cls.subject2 = Subject("Б1.Б.24", "Математический анализ",
                               1, 144, cls.specialization2)
        cls.examDate1 = date(2022, 3, 25)
        cls.examDate2 = date(2022, 5, 25)
        cls.exam1 = Exam(cls.subject1, cls.examDate1, 2022,
                         "Иванов Иван Иванович", cls.group1)
        cls.exam2 = Exam(cls.subject2, cls.examDate2, 2022,
                         "Петров Петр Петрович", cls.group2)
        cls.examPoints1 = ExamPoints(cls.student1, 65.4, 12.3, cls.exam1)
        cls.examPoints2 = ExamPoints(cls.student2, 45.6, 23.1, cls.exam2)
        cls.institute = Institute()
        cls.institute.add_exam_result(cls.examPoints1)
        cls.institute.add_exam_result(cls.examPoints2)

    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования",
                          1, 144, specialization)
        examDate = date(2022, 3, 25)
        group = Group("М-ФИИТ-21", 2021, specialization)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович", group)
        examResults = self.institute.get_exam_results(exam)
        self.assertIn(type(examResults), [ExamPoints, type(None)])
        # if examResults != None and len(examResults) != 0:
        #     self.assertEquals(type(examResults[0]), ExamPoints)

    def test_2(self):
        exam = "abcd"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam_results(exam)

    def test_3(self):
        exam = None
        with self.assertRaises(Exception) as context:
            self.institute.get_exam_results(exam)


if __name__ == '__main__':
    unittest.main()
