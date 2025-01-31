import unittest
import logging
import module_12_4_1

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = module_12_4_1.Runner("John", speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = module_12_4_1.Runner(123, speed=5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

if __name__ == '__main__':
    unittest.main()