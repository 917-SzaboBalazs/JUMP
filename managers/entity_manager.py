import pygame
from entities import Player

class EntityManager:

    def __init__(self, screen) -> None:
        self.__gravity_const = 0.95

        self.__all_entities = pygame.sprite.Group()
        self.__screen = screen

        self.add_entity(
            Player(x=50, y=200, width=50, height=80)
            )

    def get_all_entities(self):
        return self.__all_entities

    def add_entity(self, entity):
        self.__all_entities.add(entity)

    def update_entities(self):
        self.__all_entities.update()
        self._gravity()
        self._keep_on_the_screen()

    def draw_entities(self, screen):
        self.__all_entities.draw(screen)

    def _gravity(self):

        for entity in self.__all_entities:
            curr_speed_y = entity.get_speed()['speed_y']

            entity.set_speed(speed_y=curr_speed_y + self.__gravity_const)

    def _keep_on_the_screen(self):
        for entity in self.__all_entities:

            if entity.rect.bottom > self.__screen.get_size()[1]:
                entity.rect.bottom = self.__screen.get_size()[1]
                entity.set_speed(speed_y=0)