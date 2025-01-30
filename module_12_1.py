import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('Viktor')

        for _ in range(10):
            runner.walk()
        else:
            self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Vikram')
        for _ in range(10):
            runner.run()
        else:
            self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner('Viktor')
        runner_2 = Runner('Vikram')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        else:
            self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
