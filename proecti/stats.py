class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open("high_scote.txt", "r") as f:
            self.high_score = int(f.readline()) # рекорд который будет записываться отдельно


    def reset_stats(self):
        """статистика изменяется во время игры"""
        self.guns_left = 2 # жизни
        self.score = 0
