import pygame

class EntityManager:

    def __init__(self, screen) -> None:
        self.__gravity_const = 0.95

        self._all_entities = pygame.sprite.Group()
        self._screen = screen

    def update(self):
        self._gravity()
        self._all_entities.update()

    def draw(self):
        self._all_entities.draw(self._screen)

    def _gravity(self):

        for entity in self._all_entities:
            curr_speed_y = entity.get_speed()['speed_y']

            if entity.rect.bottom + curr_speed_y >= self._screen.get_size()[1]:
                entity.rect.bottom = self._screen.get_size()[1]
                entity.set_speed(speed_y=0)
            else:
                entity.set_speed(speed_y=curr_speed_y + self.__gravity_const)
