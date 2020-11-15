import unittest
import FileClass


class FileObjectCreated(unittest.TestCase):

    def setUp(self):
        print("creating file")
        self.file_ok = FileClass.FileClassObject()

    def test_if_file_created(self):
        self.assertIsInstance(self.file_ok, FileClass.FileClassObject)

    def tearDown(self):
        self.file_ok = None


class CreatePersonObject(unittest.TestCase):

    def setUp(self):
        print("creating person")
        self.my_person = FileClass.Person("melle", "rupani", 10)
        self.my_file = FileClass.FileClassObject

    def test_if_legit_person(self):
        # test if my_person object is instance of Person class
        self.assertIs(self.my_person.dob, self.my_person)
