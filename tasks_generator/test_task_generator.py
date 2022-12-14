# pylint: skip-file
"""
Checks the first task
"""
import unittest
from tasks_generator.tasks_gen import Generator
from tasks_generator.tasks_gen import TextProcessor

class GenerateTest(unittest.TestCase):
    """
    Tests generation of tasks
    """
    @classmethod
    def setUpClass(cls):
        cls.tasks_generator = Generator(TextProcessor())

    def test_generation_of_task_1_ideal(self):
        expected = ['рада Я' or 'Я рада']
        actual = self.tasks_generator.task_1(['Я рада'])
        if actual in expected:
            self.assertEqual(*expected, actual)

    def test_generation_of_task_1_not_ideal(self):
        expected = ['идет Время' or 'Время идет']
        actual = self.tasks_generator.task_1(['Время идет', '', [], {}, 1, 0.34, None, True])
        if actual in expected:
            self.assertEqual(*expected, actual)

    def test_generation_of_task_2_ideal(self):
        expected = 'Завтра я быть покупать машину. Они очень громко смеяться'
        actual = self.tasks_generator.task_2(['Завтра я буду покупать машину', 'Они очень громко смеялись'])
        self.assertEqual(expected, actual)

    def test_generation_of_task_2_not_ideal(self):
        expected = 'Вы взять его с собой'
        actual = self.tasks_generator.task_2(['Вы возьмете его с собой', '', [], {}, 1, None])
        self.assertEqual(expected, actual)

    def test_generation_of_task_3_ideal(self):
        expected = [['Когда мы идем гулять, мы', 'играть в футбол'], ['Они хотят', 'обычно берем с собой зонт']\
                    or ['Когда мы идем гулять, мы', 'обычно берем с собой зонт'], ['Они хотят', 'играть в футбол']]
        actual = self.tasks_generator.task_3(['Когда мы идем гулять, мы обычно берем с собой зонт',
                                              'Они хотят играть в футбол'])
        if actual in expected:
            self.assertEqual(expected, actual)

    def test_generation_of_task_3_not_ideal(self):
        expected = [['На обед', 'он есть рыбу']]
        actual = self.tasks_generator.task_3(['На обед он есть рыбу', '', [], {}, 1, None])
        self.assertEqual(expected, actual)

    def test_generation_of_task_4_ideal(self):
        expected = [['(1) хотим играть в футбол', ['Мы']] or ['Мы (1) играть в футбол', ['хотим']]
                    or ['Мы хотим (1) в футбол', ['играть']] or ['Мы хотим играть (1) футбол', ['в']]
                    or ['Мы хотим играть в (1)', ['футбол']]]
        actual = self.tasks_generator.task_4(['Мы хотим играть в футбол'])
        if actual in expected:
            self.assertEqual(*expected, actual)

    def test_generation_of_task_4_not_ideal(self):
        expected = [['(1) в футбол', ['Играем']] or ['Играем (1) футбол', ['в']]
                    or ['Играем в (1) ', ['футбол']]]
        actual = self.tasks_generator.task_4(['Играем в футбол', '', [], {}, 1, None])
        if actual in expected:
            self.assertEqual(*expected, actual)
