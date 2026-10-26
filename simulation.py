import pygame
from pygame import Surface, Vector2

from celestial_object import CelestialObject
from constants import METERS_TO_PIXELS


def world_to_screen(surface: pygame.Surface, pos: pygame.Vector2):
    return (pygame.Vector2(pos.x, -pos.y)) + pygame.Vector2(surface.size) / 2


class Simulation:
    def __init__(self, gravitational_constant: float) -> None:
        self.objects: list[CelestialObject] = []
        self.G: float = gravitational_constant

    def add(self, body: CelestialObject) -> None:
        self.objects.append(body)

    def get_force(self, body1: CelestialObject, body2: CelestialObject) -> Vector2:
        displacement: Vector2 = body2.pos - body1.pos
        distance_squared: float = displacement.magnitude_squared()
        force: float = (self.G * body1.mass * body2.mass) / distance_squared
        return force * displacement.normalize()

    def update_force(self, body: CelestialObject) -> None:
        body.reset_force()
        for other in self.objects:
            if other is body:
                continue
            body.add_force(self.get_force(body, other))

    def update(self, dt: float) -> None:
        for body in self.objects:
            self.update_force(body)
            body.update_acceleration()
            body.update_velocity(dt)
            body.update_pos(dt)

    def draw(self, surface: Surface) -> None:
        for body in self.objects:
            pygame.draw.aacircle(
                    surface,
                    body.color,
                    world_to_screen(surface, body.pos * METERS_TO_PIXELS),
                    body.radius,
            )
