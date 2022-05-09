import unittest
from specialization import Specialization
from institute import Institute


class TestClassSpecialization(unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", specialization.name)


class TestAddSpecialization(unittest.TestCase):
    def test_1(self):  # CORRECT
        specialization = Specialization("ФИИТ")
        institute = Institute()
        institute.add_specialization(specialization)
        self.assertEqual(len(institute.specializations), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_specialization(None)  # specialization is null
        self.assertTrue(
            'Specialization must not be null' in str(context.exception))
        self.assertEqual(len(institute.specializations), 0)

    def test_3(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_specialization(1)  # wrong type
        self.assertTrue(
            'Wrong type: must be Specialization' in str(context.exception))
        self.assertEqual(len(institute.specializations), 0)

    def test_4(self):  # INCORRECT
        specialization = Specialization("")  # empty specialization name
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_specialization(specialization)
        self.assertTrue('Empty name' in str(context.exception))
        self.assertEqual(len(institute.specializations), 0)

    def test_5(self):  # CORRECT
        specialization1 = Specialization("ФИИТ")
        specialization2 = Specialization("ИВТ")
        institute = Institute()
        institute.add_specialization(specialization1)
        institute.add_specialization(specialization2)
        self.assertEqual(len(institute.specializations), 2)

    def test_6(self):  # INCORRECT
        specialization1 = Specialization("ФИИТ")
        specialization2 = Specialization("ФИИТ")  # re-entry
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_specialization(specialization1)
            institute.add_specialization(specialization2)
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.specializations), 1)


class TestGetSpecialization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specialization1 = Specialization("ФИИТ")
        cls.specialization2 = Specialization("ИВТ")
        cls.institute = Institute()
        cls.institute.add_specialization(cls.specialization1)
        cls.institute.add_specialization(cls.specialization2)

    def test_1(self):  # CORRECT
        spec = self.institute.get_specialization("ФИИТ")
        self.assertIn(type(spec), [Specialization, type(None)])
        self.assertEqual(spec.name,
                         self.specialization1.name)

    def test_2(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_specialization("")

    def test_3(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_specialization(1234)

    def test_4(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_specialization(None)


if __name__ == '__main__':
    unittest.main()
