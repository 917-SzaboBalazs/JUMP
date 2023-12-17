import pygame
from assets import colors
from entities import Player

class GameManager:

    def __init__(self, width, height, caption, fps=60, fullscreen=False) -> None:
        self.__width = width
        self.__height = height
        self.__caption = caption
        self.__fps = fps
        self.__fullscreen = fullscreen

        self.__all_sprites = pygame.sprite.Group()

    def run(self):
        pygame.init()

        if self.__fullscreen:
            self.__screen = pygame.display.set_mode((self.__width, self.__height), pygame.FULLSCREEN)
        else:
            self.__screen = pygame.display.set_mode((self.__width, self.__height))

        pygame.display.set_caption(self.__caption)

        self._initialize()

        done = False
        clock = pygame.time.Clock()

        while not done:

            done = self._process_events()

            self._run_logic()

            self._display_frame()

            clock.tick(self.__fps)

    def _initialize(self):
        player = Player(50, 950, 50, 80)
        self.__all_sprites.add(player)

    def _process_events(self) -> bool:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            
        return False

    def _run_logic(self) -> None:
        pass

    def _display_frame(self) -> None:
        self.__screen.fill(color=colors.WHITE)

        self.__all_sprites.draw(self.__screen)

        pygame.display.flip()
