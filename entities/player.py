import pygame
from assets import colors

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color=colors.RED):

        super().__init__()

        self.__width = width
        self.__height = height
        self.__color = color

        self.image = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.__color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        