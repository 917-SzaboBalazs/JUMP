import pygame
from .entity_manager import EntityManager
from assets import Player

class PlayerManager(EntityManager):

    def __init__(self, screen: pygame.Surface) -> None:
        """
        Initializes a PlayerManager with the specified screen.

        @param screen: The pygame Surface representing the screen.
        @return: None
        """
        super().__init__(screen=screen)

        self.__player = Player(x=50, y=200, width=50, height=80)

        self._all_entities.add(self.__player)
    
    def do_jump(self) -> None:
        """
        Initiates a jump for the player.

        @return: None
        """
        self.__player.jump()

    def move_left(self) -> None:
        """
        Initiates movement to the left for the player.

        @return: None
        """
        self.__player.move_left()

    def move_right(self) -> None:
        """
        Initiates movement to the right for the player.

        @return: None
        """
        self.__player.move_right()

    def stop_moving(self, key: int) -> None:
        """
        Stops horizontal movement for the player based on the key pressed.

        @param key: The pygame key code.
        @return: None
        """
        speed_x = self.__player.get_speed()['speed_x']

        if key == pygame.K_a and speed_x < 0:
            self.__player.stop()
        elif key == pygame.K_d and speed_x > 0:
            self.__player.stop()
