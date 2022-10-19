# pylint: skip-file
"""
Checks the first task
"""
import unittest
from tasks_gen import Generator
from tasks_gen import TextProcessor

class GenerateTest(unittest.TestCase):
    """
    Tests generation of tasks
    """
    @classmethod
    def setUpClass(cls):
        cls.tasks_generator = Generator(TextProcessor())

    def test_generation_of_task_one(self):
        expected = 'рада Я'
        actual = self.tasks_generator.task_1(['Я рада'])
        self.assertEqual(expected, actual)



