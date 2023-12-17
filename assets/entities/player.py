import pygame
from assets import colors

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color=colors.RED):

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

        self.__has_double_jump = True

    def update(self):
        self.rect.x += self.__speed_x
        self.rect.y += self.__speed_y
        
    def set_speed(self, **kwargs):
        if 'speed_x' in kwargs:
            self.__speed_x = kwargs['speed_x']

        if 'speed_y' in kwargs:
            self.__speed_y = kwargs['speed_y']

    def get_speed(self):
        return {
            'speed_x': self.__speed_x,
            'speed_y': self.__speed_y
        }

    def jump(self):
        if self.__speed_y == 0:
            self.__speed_y = -20
            self.__has_double_jump = True

        elif self.__has_double_jump:
            self.__speed_y = -15
            self.__has_double_jump = False

    def move_left(self):
        self.__speed_x = -5

    def move_right(self):
        self.__speed_x = 5

    def stop(self):
        self.__speed_x = 0