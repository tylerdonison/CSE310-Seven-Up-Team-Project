from constants import *

class Health():
    def __init__(self, health) -> None:
        self._health = health
        self._draw_health()

    def decrement_health(self) -> None:
        self._health -= 1
        self._draw_health()

    def _draw_health(self) -> None:
        text = STATS_FONT.render(f"Player health: {self._health}", 1, WHITE)
        WIN.blit(text, (WIDTH - 250, 0))
        pygame.display.update()