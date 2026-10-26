# Example file showing a basic pygame "game loop"
import pygame

import constants
from celestial_object import CelestialObject
from simulation import Simulation

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

simulation: Simulation = Simulation(constants.GRAVITATIONAL_CONSTANT)

sun: CelestialObject = CelestialObject(
        'Sun',
        40,
        constants.SUN_MASS,
        '#FFC400',
        (0, 0),
        (0, 0),
)
simulation.add(sun)

mercury: CelestialObject = CelestialObject(
        'Mecury',
        10,
        constants.MERCURY_MASS,
        '#ADB0C0',
        (0.387098 * constants.ASTRONOMICAL_UNIT, 0),
        (0, 47_360),
)
simulation.add(mercury)

venus: CelestialObject = CelestialObject(
        'Venus',
        15,
        constants.VENUS_MASS,
        '#FF9D78',
        (0.723332 * constants.ASTRONOMICAL_UNIT, 0),
        (0, 35_020),
)
simulation.add(venus)

earth: CelestialObject = CelestialObject(
        'Earth',
        25,
        constants.EARTH_MASS,
        '#0089FF',
        (constants.ASTRONOMICAL_UNIT, 0),
        (0, 29_782),
)
simulation.add(earth)

mars: CelestialObject = CelestialObject(
        'Mars',
        20,
        constants.MARS_MASS,
        '#FF4564',
        (1.523680 * constants.ASTRONOMICAL_UNIT, 0),
        (0, 24_070),
)
simulation.add(mars)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('#1B1B26')

    simulation.update(constants.dt)
    simulation.draw(screen)

    pygame.display.flip()

    clock.tick(constants.FPS)

pygame.quit()
