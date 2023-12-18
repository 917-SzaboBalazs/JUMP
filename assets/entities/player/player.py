import pygame
import assets.constants.colors as colors
from assets.entities.entity import Entity
from typing import Tuple, Dict, Union

class Player(Entity):

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
        super().__init__(x, y, width, height, color)

        self.__has_double_jump = False

    def jump(self) -> None:
        """
        Makes the player jump. Allows for a double jump if not used consecutively.

        @return: None
        """
        if self._speed_y == 0:
            self._speed_y = -20
            self.__has_double_jump = True
        elif self.__has_double_jump:
            self._speed_y = -15
            self.__has_double_jump = False

    def move_left(self) -> None:
        """
        Moves the player to the left by setting a negative horizontal speed.

        @return: None
        """
        self._speed_x = -5

    def move_right(self) -> None:
        """
        Moves the player to the right by setting a positive horizontal speed.

        @return: None
        """
        self._speed_x = 5

    def stop(self) -> None:
        """
        Stops the horizontal movement of the player by setting the horizontal speed to zero.

        @return: None
        """
        self._speed_x = 0
