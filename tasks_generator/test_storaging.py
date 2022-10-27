# pylint: skip-file
"""
Checks the storaging
"""

import unittest
from tasks_generator.tasks_gen import TextProcessor
from tasks_generator.tasks_gen import Generator
from tasks_generator.tasks_gen import Storage

class SaveTasksTest(unittest.TestCase):
    """
    Storaging
    """
    @classmethod
    def setUpClass(cls):
        cls.tasks_generator = Generator(TextProcessor())
        cls.saver = Storage(Generator(TextProcessor()))

    def test_storage(self):
        expected = 0
        first_thing_to_save = self.tasks_generator.getting_texts()
        second_thing_to_save = self.tasks_generator.task_1(['Я рада'])
        actual = self.saver.storage_all(first_thing_to_save, second_thing_to_save)
        self.assertEqual(expected, actual)

