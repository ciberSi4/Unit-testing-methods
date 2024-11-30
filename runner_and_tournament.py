class Runner:
    def __init__(self, name, speed=5):
        # Инициализируем объект класса Runner с именем и скоростью.
        # По умолчанию скорость равна 5, если она не передана явно.
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        # При каждом вызове метода run увеличиваем дистанцию на удвоенное значение скорости.
        self.distance += self.speed * 2

    def walk(self):
        # При каждом вызове метода walk увеличиваем дистанцию на значение скорости.
        self.distance += self.speed

    def __str__(self):
        # Метод, возвращающий строку с именем бегуна при преобразовании объекта в строку.
        return self.name

    def __eq__(self, other):
        # Определяем поведение оператора равенства для сравнения с другим объектом.
        # Если другой объект является строкой, то сравниваем имена.
        if isinstance(other, str):
            return self.name == other
        # Если другой объект тоже является Runner'ом, то сравниваем их имена.
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        # Инициализируем объект турнира с заданной дистанцией и списком участников.
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        # Создаем пустой словарь для хранения информации о финишировавших участниках.
        finishers = {}
        # Переменная place хранит текущее место участника.
        place = 1
        # Пока есть участники, продолжаем цикл.
        while self.participants:
            # Проходимся по всем участникам.
            for participant in self.participants:
                # Вычисляем оставшуюся дистанцию до финиша.
                remaining_distance = self.full_distance - participant.distance
                # Если оставшаяся дистанция меньше или равна тому расстоянию, которое участник может пробежать за один раз...
                if remaining_distance <= participant.speed * 2:
                    # То добавляем всю оставшуюся дистанцию к общей дистанции участника.
                    participant.distance += remaining_distance
                else:
                    # Иначе просто выполняем обычный бег.
                    participant.run()

                # Если участник достиг полной дистанции...
                if participant.distance >= self.full_distance:
                    # Добавляем информацию о нем в словарь finishers с указанием места.
                    finishers[place] = participant
                    # Инкрементируем место.
                    place += 1
                    # Удаляем участника из списка участников, так как он уже финишировал.
                    self.participants.remove(participant)

        # Возвращаем словарь с информацией о финишировавших участниках.
        return finishers