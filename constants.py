GRAVITATIONAL_CONSTANT: float = 6.6743e-11
ASTRONOMICAL_UNIT: float = 149_597_870_700

SUN_MASS: float = 1.988416e30
MERCURY_MASS: float = 3.3011e23
VENUS_MASS: float = 4.86731e24
EARTH_MASS: float = 5.9722e24
MARS_MASS: float = 6.4171e23

METERS_TO_PIXELS: float = 200 / ASTRONOMICAL_UNIT

FPS: int = 60
TIMESTEP = 60 * 60 * 24 * 5  # one second in realtime equals 5 days in simulation
dt = TIMESTEP / FPS
