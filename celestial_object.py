from pygame import Color, Vector2
from pygame.typing import ColorLike, SequenceLike


class CelestialObject:
    def __init__(
            self,
            name: str,
            radius: int,
            mass: float,
            color: ColorLike,
            pos: SequenceLike[float] = (0, 0),
            velocity: SequenceLike[float] = (0, 0),
    ) -> None:
        self.name: str = name
        self.radius: int = radius
        self.mass: float = mass
        self.color: Color = Color(color)
        self.pos: Vector2 = Vector2(pos)
        self.velocity: Vector2 = Vector2(velocity)
        self.acceleration: Vector2 = Vector2()
        self.force: Vector2 = Vector2()

    def reset_force(self) -> None:
        self.force.update(0, 0)

    def add_force(self, force: Vector2) -> None:
        self.force += force

    def update_acceleration(self) -> None:
        self.acceleration.update(self.force / self.mass)

    def update_velocity(self, dt: float) -> None:
        self.velocity += self.acceleration * dt

    def update_pos(self, dt: float) -> None:
        self.pos += self.velocity * dt

    def __repr__(self) -> str:
        return f'CelestialObject({self.name})'
