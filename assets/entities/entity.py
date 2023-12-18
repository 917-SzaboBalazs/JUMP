import pygame
from typing import Tuple, Dict, Union

class Entity(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, color: Tuple[int, int, int]) -> None:
        """
        Initializes an Entity object with the specified position, dimensions, and color.

        @param x: The x-coordinate of the entity's initial position.
        @param y: The y-coordinate of the entity's initial position.
        @param width: The width of the entity's sprite.
        @param height: The height of the entity's sprite.
        @param color: The RGB color tuple representing the entity's sprite color.
        @return: None
        """
        super().__init__()

        self._width = width
        self._height = height
        self._color = color

        self._speed_x = 0
        self._speed_y = 0

        self.image = pygame.Surface((self._width, self._height))
        self.image.fill(self._color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        """
        Updates the entity's position based on its speed.

        @return: None
        """
        self.rect.x += self._speed_x
        self.rect.y += self._speed_y

    def set_speed(self, **kwargs: Dict[str, Union[int, float]]) -> None:
        """
        Sets the horizontal and vertical speed of the entity.

        @param kwargs: A dictionary containing speed values. Possible keys are 'speed_x' and 'speed_y'.
        @return: None
        """
        if 'speed_x' in kwargs:
            self._speed_x = kwargs['speed_x']

        if 'speed_y' in kwargs:
            self._speed_y = kwargs['speed_y']

    def get_speed(self) -> Dict[str, Union[int, float]]:
        """
        Retrieves the current horizontal and vertical speed of the entity.

        @return: A dictionary containing 'speed_x' and 'speed_y'.
        """
        return {
            'speed_x': self._speed_x,
            'speed_y': self._speed_y
        }
