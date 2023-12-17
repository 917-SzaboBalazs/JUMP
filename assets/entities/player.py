import pygame
from assets import colors
from typing import Tuple, Dict, Union

class Player(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, color: Tuple[int, int, int] = colors.RED) -> None:
        """
        Initializes a Player object with the specified position, dimensions, and color.

        @param x: The x-coordinate of the player's initial position.
        @param y: The y-coordinate of the player's initial position.
        @param width: The width of the player's sprite.
        @param height: The height of the player's sprite.
        @param color: The RGB color tuple representing the player's sprite color.
            Default is colors.RED.
        @return: None
        """
        super().__init__()

        self.__width = width
        self.__height = height
        self.__color = color

        self.__speed_x = 0
        self.__speed_y = 0

        self.image = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.__color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.__has_double_jump = False

    def update(self) -> None:
        """
        Updates the player's position based on its speed.

        @return: None
        """
        self.rect.x += self.__speed_x
        self.rect.y += self.__speed_y

    def set_speed(self, **kwargs: Dict[str, Union[int, float]]) -> None:
        """
        Sets the horizontal and vertical speed of the player.

        @param kwargs: A dictionary containing speed values. Possible keys are 'speed_x' and 'speed_y'.
        @return: None
        """
        if 'speed_x' in kwargs:
            self.__speed_x = kwargs['speed_x']

        if 'speed_y' in kwargs:
            self.__speed_y = kwargs['speed_y']

    def get_speed(self) -> Dict[str, Union[int, float]]:
        """
        Retrieves the current horizontal and vertical speed of the player.

        @return: A dictionary containing 'speed_x' and 'speed_y'.
        """
        return {
            'speed_x': self.__speed_x,
            'speed_y': self.__speed_y
        }

    def jump(self) -> None:
        """
        Makes the player jump. Allows for a double jump if not used consecutively.

        @return: None
        """
        if self.__speed_y == 0:
            self.__speed_y = -20
            self.__has_double_jump = True
        elif self.__has_double_jump:
            self.__speed_y = -15
            self.__has_double_jump = False

    def move_left(self) -> None:
        """
        Moves the player to the left by setting a negative horizontal speed.

        @return: None
        """
        self.__speed_x = -5

    def move_right(self) -> None:
        """
        Moves the player to the right by setting a positive horizontal speed.

        @return: None
        """
        self.__speed_x = 5

    def stop(self) -> None:
        """
        Stops the horizontal movement of the player by setting the horizontal speed to zero.

        @return: None
        """
        self.__speed_x = 0
