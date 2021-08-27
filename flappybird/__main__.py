import pygame
from pygame.constants import QUIT

from flappybird.core.scene import SceneMananger

DISPLAY = (600, 400)
DEPTH = 0
FLAGS = 0


def main() -> None:
    """Start the main game."""
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    timer = pygame.time.Clock()
    running = True

    manager = SceneMananger()

    while running:
        timer.tick(60)

        if pygame.event.get(QUIT):
            running = False
            return
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
