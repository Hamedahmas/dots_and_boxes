# game.py
class GameState:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.edges = set()  # لبه‌های گرفته شده
        self.boxes = {}     # امتیاز هر خانه
        self.current_player = 1
        self.score = {1: 0, -1: 0}

    def get_possible_moves(self):
        all_edges = self._generate_all_edges()
        return [e for e in all_edges if e not in self.edges]

    def make_move(self, edge):
        self.edges.add(edge)
        completed_box = self._check_box_completion(edge)
        if completed_box:
            self.score[self.current_player] += len(completed_box)
        else:
            self.current_player *= -1

    def is_game_over(self):
        return len(self.edges) == len(self._generate_all_edges())

    def _generate_all_edges(self):
        edges = set()
        for r in range(self.rows + 1):
            for c in range(self.cols):
                edges.add(((r, c), (r, c + 1)))
        for r in range(self.rows):
            for c in range(self.cols + 1):
                edges.add(((r, c), (r + 1, c)))
        return edges

    def _check_box_completion(self, edge):
        # بررسی اینکه آیا خانه‌ای کامل شده یا نه
        completed = []
        # باید بررسی بشه آیا این حرکت باعث پر شدن ۴ لبه یک خانه شده
        # برای ساده‌سازی، این بخش فقط پایه‌گذاری شده
        return completed

    def clone(self):
        new_state = GameState(self.rows, self.cols)
        new_state.edges = set(self.edges)
        new_state.score = dict(self.score)
        new_state.current_player = self.current_player
        return new_state
