from constants import *

class Score():
    def __init__(self) -> None:
        self._score = 0
        self._draw_score()

    def update_score(self, added_score) -> None:
        self._score += added_score
        self._draw_score()

    def _draw_score(self) -> None:
        text = STATS_FONT.render(f"Player score: {self._score}", 1, WHITE)
        WIN.blit(text, (30, 0))
        pygame.display.update()