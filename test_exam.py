import unittest
from datetime import date
from subject import Subject
from specialization import Specialization
from exam import Exam
from institute import Institute


class TestClassExam(unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("1", "2", 3, 4, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        self.assertEqual(subject, exam.subject)
        self.assertEqual(examDate, exam.examDate)
        self.assertEqual(2022, exam.year)
        self.assertEqual("Иванов Иван Иванович", exam.lecturerFio)


class TestAddExam(unittest.TestCase):
    def test_1(self):  # CORRECT
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования",
                          1, 144, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        institute = Institute()
        institute.add_exam(exam)
        self.assertEqual(len(institute.exams), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam(None)  # exam is null
        self.assertTrue('Exam must not be null' in str(context.exception))
        self.assertEqual(len(institute.exams), 0)

    def test_3(self):  # CORRECT
        specialization1 = Specialization("ФИИТ")
        specialization2 = Specialization("ИВТ")
        subject1 = Subject("Б1.Б.22", "Основы программирования",
                           1, 144, specialization1)
        subject2 = Subject("Б1.Б.22", "Основы программирования",
                           1, 144, specialization2)
        examDate = date(2022, 5, 5)
        exam1 = Exam(subject1, examDate, 2022, "Иванов Иван Иванович")
        exam2 = Exam(subject2, examDate, 2022, "Петров Петр Петрович")
        institute = Institute()
        institute.add_exam(exam1)
        institute.add_exam(exam2)
        self.assertEqual(len(institute.exams), 2)

    def test_4(self):  # INCORRECT
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования",
                          1, 144, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam(exam)
            institute.add_exam(exam)  # re-entry
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.exams), 1)


class TestGetExam(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specialization1 = Specialization("ФИИТ")
        cls.specialization2 = Specialization("ИВТ")
        cls.subject1 = Subject("Б1.Б.22", "Основы программирования",
                           1, 144, cls.specialization1)
        cls.subject2 = Subject("Б1.Б.24", "Математический анализ",
                           1, 144, cls.specialization2)
        cls.examDate1 = date(2022, 3, 25)
        cls.examDate2 = date(2022, 5, 25)
        cls.exam1 = Exam(cls.subject1, cls.examDate1, 2022, "Иванов Иван Иванович")
        cls.exam2 = Exam(cls.subject2, cls.examDate2, 2022, "Петров Петр Петрович")
        cls.institute = Institute()
        cls.institute.add_exam(cls.exam1)
        cls.institute.add_exam(cls.exam2)

    def test_1(self):  # CORRECT
        group_name = "ФИИТ"
        subj_name = "Основы программирования"
        exam = self.institute.get_exam(group_name, subj_name, date(2022, 3, 25))
        self.assertIn(type(exam), [Exam, type(None)])
        self.assertEqual(exam.examDate, self.examDate1)

    def test_2(self):  # INCORRECT
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam("", subj_name, date(2022, 3, 25))

    def test_3(self):  # INCORRECT
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(1234, subj_name, date(2022, 3, 25))

    def test_4(self):  # INCORRECT
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(None, subj_name, date(2022, 3, 25))

    def test_5(self):  # INCORRECT
        group_name = "ФИИТ"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, "", date(2022, 3, 25))

    def test_6(self):  # INCORRECT
        group_name = "ФИИТ"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, 1234, date(2022, 3, 25))

    def test_7(self):  # INCORRECT
        group_name = "ФИИТ"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, None, date(2022, 3, 25))

    def test_8(self):  # INCORRECT
        group_name = "ФИИТ"
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, subj_name, "2022, 3, 25")

    def test_9(self):  # INCORRECT
        group_name = "ФИИТ"
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, subj_name, "2022/03/25")

    def test_10(self):  # INCORRECT
        group_name = "ФИИТ"
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, subj_name, 2022)

    def test_11(self):  # INCORRECT
        group_name = "ФИИТ"
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, subj_name, None)

    def test_12(self):  # INCORRECT
        institute = Institute()
        group_name = "ФИИТ"
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, subj_name, date(2024, 3, 25))

    def test_13(self):  # INCORRECT
        group_name = "ФИИТ"
        subj_name = "Основы программирования"
        with self.assertRaises(Exception) as context:
            self.institute.get_exam(group_name, subj_name, date(1024, 3, 25))


if __name__ == '__main__':
    unittest.main()
