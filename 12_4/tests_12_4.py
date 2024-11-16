import logging
import human_move
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            alexandr = human_move.Runner('Alexandr', -12)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                alexandr.walk()
            self.assertEqual(alexandr.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            boris = human_move.Runner(63)
            for _ in range(10):
                boris.run()
            self.assertEqual(boris.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для имени объекта Runner')

    def test_challenge(self):
        alexandr = human_move.Runner('Alexandr')
        for _ in range(10):
            alexandr.walk()
        boris = human_move.Runner('Boris')
        for _ in range(10):
            boris.run()
        self.assertNotEqual(alexandr.distance, boris.distance)



logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
