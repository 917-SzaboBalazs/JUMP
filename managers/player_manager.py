import pygame
from .entity_manager import EntityManager
from entities import Player

class PlayerManager(EntityManager):

    def __init__(self, screen):
        super().__init__(screen=screen)

        self.__player = Player(x=50, y=200, width=50, height=80)

        self._all_entities.add(
            self.__player
        )
    
    def do_jump(self):
        self.__player.jump()

    def move_left(self):
        self.__player.move_left()

    def move_right(self):
        self.__player.move_right()

    def stop_moving(self, key):
        speed_x = self.__player.get_speed()['speed_x']

        if key == pygame.K_a and speed_x < 0:
            self.__player.stop()
        
        elif key == pygame.K_d and speed_x > 0:
            self.__player.stop()
