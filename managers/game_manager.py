import pygame
from assets import colors
from .player_manager import PlayerManager

class GameManager:

    def __init__(self, width, height, caption, fps=60, fullscreen=False) -> None:
        self.__width = width
        self.__height = height
        self.__caption = caption
        self.__fps = fps
        self.__screen = None
        self.__fullscreen = fullscreen


        # Managers

        self.__player_manager = None

    def run(self):
        self._initialize()

        done = False
        clock = pygame.time.Clock()

        while not done:

            done = self._process_events()

            self._run_logic()

            self._display_frame()

            clock.tick(self.__fps)

    def _initialize(self):
        pygame.init()

        if self.__fullscreen:
            self.__screen = pygame.display.set_mode((self.__width, self.__height), pygame.FULLSCREEN)
        else:
            self.__screen = pygame.display.set_mode((self.__width, self.__height))

        self.__player_manager = PlayerManager(screen=self.__screen)

        pygame.display.set_caption(self.__caption)

    def _process_events(self) -> bool:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.__player_manager.do_jump()

                elif event.key == pygame.K_a:
                    self.__player_manager.move_left()

                elif event.key == pygame.K_d:
                    self.__player_manager.move_right()

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_d):
                    self.__player_manager.stop_moving(key=event.key)
            
        return False

    def _run_logic(self) -> None:
        self.__player_manager.update()

    def _display_frame(self) -> None:
        self.__screen.fill(color=colors.WHITE)

        self.__player_manager.draw()

        pygame.display.flip()
