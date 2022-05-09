import unittest
from student import Student
from institute import Institute


class TestClassStudent(unittest.TestCase):
    def test_1(self):
        student = Student("Федоров Байытаан", 123456)
        self.assertEqual("Федоров Байытаан", student.fio)
        self.assertEqual(123456, student.code)


class TestAddStudent(unittest.TestCase):
    def test_1(self):  # CORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        institute = Institute()
        institute.add_student(student)
        self.assertEqual(len(institute.students), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(None)  # student is null
        self.assertTrue('Student must not be null' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_3(self):  # INCORRECT
        student = Student("ФедоровБайытаанПавлович",
                          123456)  # incorrect student name
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue('Incorrect name' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_4(self):  # INCORRECT
        student = Student("", 123456)  # empty student name
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue('Empty name' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_5(self):  # INCORRECT
        student = Student(1234, 123456)  # wrong student name type
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue('Wrong type: must be str' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_6(self):  # INCORRECT
        student = Student(None, 123456)  # empty student name
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Student name must not be null' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_7(self):  # CORRECT
        student1 = Student("Федоров Байытаан Павлович", 123456)
        student2 = Student("Иванов Иван Иванович", 456789)
        institute = Institute()
        institute.add_student(student1)
        institute.add_student(student2)
        self.assertEqual(len(institute.students), 2)

    def test_8(self):  # INCORRECT
        student1 = Student("Федоров Байытаан Павлович", 123456)
        student2 = Student("Федоров Байытаан Павлович", 123456)  # re-entry
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student1)
            institute.add_student(student2)
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.students), 1)

    def test_9(self):  # INCORRECT
        # wrong student code type
        student = Student("Федоров Байытаан Павлович", None)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Student code must not be null' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_10(self):  # INCORRECT
        # wrong student code type
        student = Student("Федоров Байытаан Павлович", 123456.0)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Wrong type: must be integer' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_11(self):  # INCORRECT
        # wrong student code type
        student = Student("Федоров Байытаан Павлович", -123456)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Student code must not be < 0' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_12(self):  # INCORRECT
        # wrong student code type
        student = Student("Федоров Байытаан Павлович", "123456")
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Wrong type: must be integer' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_13(self):  # INCORRECT
        # student code is not 6-digit
        student = Student("Федоров Байытаан Павлович", 99999)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Student code is not 6-digit' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_14(self):  # INCORRECT
        # student code is not 6-digit
        student = Student("Федоров Байытаан Павлович", 1000000)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Student code is not 6-digit' in str(context.exception))
        self.assertEqual(len(institute.students), 0)


class TestGetStudent(unittest.TestCase):
    # def __init__(self, *args, **kwargs):
    #     self.institute = Institute()
    #     self.institute.students = [Student("Федоров Байытаан", 123456), Student("Иванов Иван", 465789)]
    #     super(TestGetStudent, self).__init__(*args, **kwargs)
    @classmethod
    def setUpClass(cls):
        cls.institute = Institute()
        cls.institute.students = [
            Student("Федоров Байытаан", 123456), Student("Иванов Иван", 465789), Student("Петров Иван", 100000), Student("Иванов Петр", 999999)]

    def test_1(self):  # CORRECT
        student = self.institute.get_student(123456)
        self.assertIn(type(student), [Student, type(None)])
        self.assertEqual(self.institute.students[0].fio, student.fio)

    def test_2(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student(None)  # code is null

    def test_3(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student(123456.0)  # code is float

    def test_4(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student(-123456)  # code < 0

    def test_5(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student("123456")  # code is not int

    def test_6(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student(1234567)  # code is not 6-digit

    def test_7(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student(12345)  # code is not 6-digit

    def test_8(self):  # CORRECT
        student = self.institute.get_student(100000)
        self.assertIn(type(student), [Student, type(None)])
        self.assertEqual(self.institute.students[2].fio, student.fio)

    def test_9(self):  # CORRECT
        student = self.institute.get_student(999999)
        self.assertIn(type(student), [Student, type(None)])
        self.assertEqual(self.institute.students[3].fio, student.fio)

    def test_10(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student(1000000)

    def test_11(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_student(99999)


if __name__ == '__main__':
    unittest.main()
