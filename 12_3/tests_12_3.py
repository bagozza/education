import unittest
import Tour


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены.')
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.ysein = Tour.Runner('Усэйн', 10)
        self.andrew = Tour.Runner('Андрей', 9)
        self.nick = Tour.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(
                {pos: runner.name for pos, runner in result.items()}
            )

    def test_run_1(self):
        self.ys_nik = Tour.Tournament(90, self.ysein, self.nick)
        result = self.ys_nik.start()
        self.all_results.append(result)
        last_1 = result[max(result.keys())]
        self.assertTrue(last_1 == 'Ник')

    def test_run_2(self):
        self.an_nick = Tour.Tournament(90, self.andrew, self.nick)
        result = self.an_nick.start()
        self.all_results.append(result)
        last_2 = result[max(result.keys())]
        self.assertTrue(last_2 == 'Ник')

    def test_run_3(self):
        self.final = Tour.Tournament(90, self.andrew, self.nick, self.ysein)
        result = self.final.start()
        self.all_results.append(result)
        last_3 = result[max(result.keys())]
        self.assertTrue(last_3 == 'Ник')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        alexandr = Tour.Runner('Alexandr')
        for _ in range(10):
            alexandr.walk()
        self.assertEqual(alexandr.distance, 50)

    def test_run(self):
        boris = Tour.Runner('Boris')
        for _ in range(10):
            boris.run()
        self.assertEqual(boris.distance, 100)

    def test_challenge(self):
        alexandr = Tour.Runner('Alexandr')
        for _ in range(10):
            alexandr.walk()
        boris = Tour.Runner('Boris')
        for _ in range(10):
            boris.run()
        self.assertNotEqual(alexandr.distance, boris.distance)
