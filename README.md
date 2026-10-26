# Solar System Simulation

This is a simple 2d simulation of the solar system.

The distances between the planets are to scale with the real solar system.
Planets radii, on the other hand, are emphasized as the real ratios will make planets much smaller
than a pixel.

## How to run the simulation?

To run the script, you have to install the **Pygame** library, specifically, **pygame-ce**.  
Use python package manager [pip](https://pip.pypa.io/en/stable/) to install pygame-ce.

```bash
pip install pygame-ce
```

To run the game, just open the terminal and type this command

```bash
python main.py
```

> [!NOTE]
> The constants.py file has variables to control the speed, size and behaviour of the simulation,
> fiddle around and have fun with it.

## Features

Don't expect an astonishing visual, the current UI is ugly. But it works well as a live wallpaper.

## what's next?

- Add the rest of the solar system (including dwarf planets)
- Add the ability to drag and zoom.
- clicking on an object will reveal some fun facts and info about it.
- add simulation speed control
- use real time positions of planets.

> That's what I have in mind for now.

## License

[MIT](https://choosealicense.com/licenses/mit/)