# Домашнее задание по теме "Методы Юнит-тестирования"
import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Статический метод, который выполняется один раз перед запуском всех тестов.
        # Создаем пустой словарь для хранения результатов всех тестов.
        cls.all_results = {}

    def setUp(self):
        # Метод, который выполняется перед каждым тестовым методом.
        # Создаем трех участников с разными именами и скоростями.
        self.usain = runner_and_tournament.Runner('Usain', 10)
        self.andrey = runner_and_tournament.Runner('Andrey', 9)
        self.nick = runner_and_tournament.Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        # Статический метод, который выполняется один раз после завершения всех тестов.
        # Выводим результаты всех тестов в удобочитаемом формате.
        for key, value in cls.all_results.items():
            print("{")
            for k, v in value.items():
                print(f"\t{k}: {v},")
            print("}")

    def test_usain_and_nick(self):
        # Тестовый метод для проверки турнира между Усэйном и Ником.
        # Создаем объект турнира с участниками Усэйн и Ник.
        tournament = runner_and_tournament.Tournament(90, self.usain, self.nick)
        # Запускаем турнир и получаем результаты.
        result = tournament.start()
        # Сохраняем результаты в общий словарь all_results под ключом 'usain_and_nick'.
        self.all_results['usain_and_nick'] = result
        # Находим последнего финишировавшего участника.
        last_place_runner = max(result.keys())
        # Проверяем, что последним финишировал Ник.
        self.assertTrue(result[last_place_runner].name == 'Nick')

    def test_andrey_and_nick(self):
        # Тестовый метод для проверки турнира между Андреем и Ником.
        # Создаем объект турнира с участниками Андрей и Ник.
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        # Запускаем турнир и получаем результаты.
        result = tournament.start()
        # Сохраняем результаты в общий словарь all_results под ключом 'andrey_and_nick'.
        self.all_results['andrey_and_nick'] = result
        # Находим последнего финишировавшего участника.
        last_place_runner = max(result.keys())
        # Проверяем, что последним финишировал Ник.
        self.assertTrue(result[last_place_runner].name == 'Nick')

    def test_all_three(self):
        # Тестовый метод для проверки турнира между всеми тремя участниками.
        # Создаем объект турнира с участниками Усэйн, Андрей и Ник.
        tournament = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nick)
        # Запускаем турнир и получаем результаты.
        result = tournament.start()
        # Сохраняем результаты в общий словарь all_results под ключом 'all_three'.
        self.all_results['all_three'] = result
        # Находим последнего финишировавшего участника.
        last_place_runner = max(result.keys())
        # Проверяем, что последним финишировал Ник.
        self.assertTrue(result[last_place_runner].name == 'Nick')


if __name__ == '__main__':
    # Запускаем тестирование, если скрипт был вызван напрямую.
    unittest.main()