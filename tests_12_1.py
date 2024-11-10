import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        alexandr = runner.Runner('Alexandr')
        for _ in range(10):
            alexandr.walk()
        self.assertEqual(alexandr.distance, 50)

    def test_run(self):
        boris = runner.Runner('Boris')
        for _ in range(10):
            boris.run()
        self.assertEqual(boris.distance, 100)

    def test_challenge(self):
        alexandr = runner.Runner('Alexandr')
        for _ in range(10):
            alexandr.walk()
        boris = runner.Runner('Boris')
        for _ in range(10):
            boris.run()
        self.assertNotEqual(alexandr.distance, boris.distance)