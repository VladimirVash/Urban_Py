import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


# Создаем класс для тестирования
class TournamentTest(unittest.TestCase):
    is_frozen = False

    # Переменная для хранения всех результатов
    all_results = {}

    # Метод, который вызывается один раз перед всеми тестами
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Инициализируем пустой словарь для хранения результатов

    # Метод, который вызывается перед каждым тестом
    def setUp(self):
        # Создаем объекты бегунов
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    # Метод, который вызывается один раз после всех тестов
    @classmethod
    def tearDownClass(cls):
        # Проходим по всем сохраненным результатам тестов
        for test_name, results in cls.all_results.items():
            # Формируем строку результата в нужном формате
            result_str = ", ".join(f"{place}: {runner.name}" for place, runner in sorted(results.items()))
            # Заменяем запятые на пробелы и выводим результат
            print(f"{{{result_str.replace(', ', ' ')}}}")

    # Вспомогательный метод для запуска турнира и проверки последнего бегуна
    def check_last_runner(self, participants, expected_last_runner_name):
        # Создаем объект турнира с заданной дистанцией и участниками
        tournament = Tournament(90, *participants)
        # Запускаем турнир и получаем результаты
        results = tournament.start()
        # Находим место последнего финишировавшего участника
        max_place = max(results.keys())
        last_runner = results[max_place]
        # Сохраняем результаты текущего теста в общем словаре
        test_name = self._testMethodName
        if test_name not in self.__class__.all_results:
            self.__class__.all_results[test_name] = {}
        self.__class__.all_results[test_name].update(results)
        # Проверяем, что последний финишировавший — это Ник
        self.assertTrue(last_runner.name == expected_last_runner_name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usain_and_nick(self):
        self.check_last_runner([self.usain, self.nick], "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nick(self):
        self.check_last_runner([self.andrey, self.nick], "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usain_andrey_and_nick(self):
        self.check_last_runner([self.usain, self.andrey, self.nick], "Ник")



class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('Viktor')

        for _ in range(10):
            runner.walk()
        else:
            self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('Vikram')
        for _ in range(10):
            runner.run()
        else:
            self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = Runner('Viktor')
        runner_2 = Runner('Vikram')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        else:
            self.assertNotEqual(runner_1.distance, runner_2.distance)