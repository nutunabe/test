import unittest
from group import Group
from specialization import Specialization
from institute import Institute


class TestClassGroup(unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, specialization)
        self.assertEqual("М-ФИИТ-21", group.name)
        self.assertEqual(2021, group.year)
        self.assertEqual(specialization, group.specialization)


class TestAddGroup(unittest.TestCase):
    def test_1(self):  # CORRECT
        specialization = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, specialization)
        institute = Institute()
        institute.add_group(group)
        self.assertEqual(len(institute.groups), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_group(None)  # group is null
        self.assertTrue('Group must not be null' in str(context.exception))
        self.assertEqual(len(institute.groups), 0)

    def test_3(self):  # INCORRECT
        specialization = Specialization("ФИИТ")
        group = Group("", 2021, specialization)  # empty group name
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_group(group)
        self.assertTrue('Empty name' in str(context.exception))
        self.assertEqual(len(institute.groups), 0)

    def test_4(self):  # CORRECT
        specialization1 = Specialization("ФИИТ")
        specialization2 = Specialization("ИВТ")
        group1 = Group("М-ФИИТ-21", 2021, specialization1)
        group2 = Group("М-ИВТ-21", 2021, specialization2)
        institute = Institute()
        institute.add_group(group1)
        institute.add_group(group2)
        self.assertEqual(len(institute.groups), 2)

    def test_5(self):  # INCORRECT
        specialization = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, specialization)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_group(group)
            institute.add_group(group)  # re-entry
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.groups), 1)


class TestGetGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specialization1 = Specialization("ФИИТ")
        cls.specialization2 = Specialization("ИВТ")
        cls.group1 = Group("М-ФИИТ-21", 2021, cls.specialization1)
        cls.group2 = Group("М-ИВТ-21", 2021, cls.specialization2)
        cls.institute = Institute()
        cls.institute.groups = [cls.group1, cls.group2]

    def test_1(self):  # CORRECT
        group = self.institute.get_group("М-ФИИТ-21")
        self.assertIn(type(group), [Group, type(None)])
        self.assertEqual(group.specialization.name,
                         self.group1.specialization.name)

    def test_2(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_group("")

    def test_3(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_group(1234)

    def test_4(self):  # INCORRECT
        with self.assertRaises(Exception) as context:
            self.institute.get_group(None)

    # def test_5(self):  # INCORRECT
    #     institute = Institute()
    #     with self.assertRaises(Exception) as context:
    #         institute.get_group("abcd")  # does not match the mask


if __name__ == '__main__':
    unittest.main()
