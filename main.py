# 1. **Определение требований и проектирование:**
#    - Разработать концепцию игры и определить основные классы и методы.
#    - Описать правила и логику игры.
#
# 2. **Создание классов:**
#    - Создать класс `Hero` с необходимыми атрибутами и методами.
#    - Создать класс `Game` для управления процессом игры.
#
# 3. **Реализация логики игры:**
#    - Реализовать метод `start` в классе `Game`, который будет управлять ходом игры.
#
# 4. **Тестирование:**
#    - Провести тестирование отдельных компонентов и всей игры в целом.
#    - Убедиться в корректности работы всех методов и логики игры.
#
# 5. **Улучшение и оптимизация:**
#    - Добавить дополнительные возможности (например, выбор уровня сложности).
#    - Оптимизировать код и улучшить пользовательский интерфейс.



import random

class Hero:
    def __init__(self, name, health=100, min_attack_power=10, max_attack_power=30):
        self.name = name
        self.health = health
        self.min_attack_power = min_attack_power
        self.max_attack_power = max_attack_power

    def attack(self, other):
        if self.is_alive():
            attack_power = random.randint(self.min_attack_power, self.max_attack_power)
            print(f"{self.name} атакует {other.name} с силой {attack_power}.")
            other.health -= attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        turn = random.choice(['player', 'computer'])  # Случайно выбираем, кто начнет

        while self.player.is_alive() and self.computer.is_alive():
            if turn == 'player':
                self.player.attack(self.computer)
                if self.computer.is_alive():
                    print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")
                else:
                    print(f"{self.computer.name} побежден!\n")
                turn = 'computer'
            else:
                self.computer.attack(self.player)
                if self.player.is_alive():
                    print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")
                else:
                    print(f"{self.player.name} побежден!\n")
                turn = 'player'

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Пример использования
if __name__ == "__main__":
    game = Game("Игрок", "Компьютер")
    game.start()