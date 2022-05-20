import unittest
from unittest.mock import patch
from io import StringIO
from student import Student
from institute import Institute
from main import main


class TestMain(unittest.TestCase):
    student1 = ['Иванов Иван Иванович', '123456']
    group1 = ['М-ФИИТ-21', '2021',
              'Фундаметельная информатики и информационные технологии']

    @patch('builtins.input', side_effect=student1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_output, mock_input):
        main(['', 'add', 'student'],)
        self.assertEqual(mock_output.getvalue(),
                         'Student(code=123456, fio=\'Иванов Иван Иванович\')\n')

    @patch('builtins.input', side_effect=group1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_output, mock_input):
        main(['', 'add', 'group'],)
        self.assertEqual(mock_output.getvalue(),
                         'Group(name=\'М-ФИИТ-21\', year=2021, specialization=Specialization(name=\'Фундаметельная информатики и информационные технологии\'))\n')


if __name__ == '__main__':
    unittest.main()
