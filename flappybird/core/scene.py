import sys

import pygame
from pygame.event import Event
from pygame_menu.menu import Menu


class Scene(object):
    """An example of Scene."""

    def __init__(self):
        pass

    def run(self) -> None:
        """Called after manager is added to the scene."""
        raise NotImplementedError

    def render(self, screen: pygame.Surface) -> None:
        """Render the scene."""
        raise NotImplementedError

    def update(self) -> None:
        """Update the scene."""
        raise NotImplementedError

    def handle_events(self, events: Event) -> None:
        """Handle event for the scene."""
        raise NotImplementedError


class MenuScene(Scene):
    """Menu scene to handle menu event."""

    def __init__(self):
        super(MenuScene, self).__init__()
        self.menu = Menu(
            "Flappy Bird",
            600,
            400,
            center_content=True,
            mouse_enabled=True,
            mouse_visible=True,
            mouse_motion_selection=True,
        )

    def run(self) -> None:
        """Called after manager is added to the scene."""
        self.menu.add.button("Play", lambda: self.manager.go_to(GameScene()))
        self.menu.add.button(
            "Leaderboard", lambda: self.manager.go_to(LeaderboardScene())
        )
        self.menu.add.button("Quit", sys.exit)

    def render(self, screen: pygame.Surface) -> None:
        """Render the scene."""
        self.menu.draw(screen)

    def update(self) -> None:
        """Update the scene."""
        pass

    def handle_events(self, events: Event) -> None:
        """Handle event for the scene."""
        self.menu.update(events)


class GameScene(Scene):
    """Game scene to display the game."""

    def __init__(self):
        super(GameScene, self).__init__()

    def run(self) -> None:
        """Called after manager is added to the scene."""
        raise NotImplementedError

    def render(self, screen: pygame.Surface) -> None:
        """Render the scene."""
        raise NotImplementedError

    def update(self) -> None:
        """Update the scene."""
        raise NotImplementedError

    def handle_events(self, events: Event) -> None:
        """Handle event for the scene."""
        raise NotImplementedError


class LeaderboardScene(object):
    """Leaderboard scene to display leaderboard."""

    def __init__(self):
        pass

    def run(self) -> None:
        """Called after manager is added to the scene."""
        raise NotImplementedError

    def render(self, screen: pygame.Surface) -> None:
        """Render the scene."""
        raise NotImplementedError

    def update(self) -> None:
        """Update the scene."""
        raise NotImplementedError

    def handle_events(self, events: Event) -> None:
        """Handle event for the scene."""
        raise NotImplementedError


class SceneMananger(object):
    """Scene mananger is to make change scene easier"""

    def __init__(self, init_scene: Scene = None):
        if not init_scene:
            init_scene = MenuScene()
        self.go_to(init_scene)

    def go_to(self, scene: Scene) -> None:
        """Change scene."""
        self.scene = scene
        self.scene.manager = self
        self.scene.run()
