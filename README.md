# Alien-game
# Space Invaders Clone

This project is a simple 2D Space Invaders clone created using Python and Pygame. Players control a spaceship to defend against waves of invading aliens, utilizing bullets to destroy them while avoiding enemy fire.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Code Structure](#code-structure)
- [Customizations](#customizations)
- [Contributing](#contributing)
- [License](#license)

## Features

**Player Movement**: Move left and right to dodge alien attacks.
**Shooting Mechanic**: Shoot bullets to eliminate aliens.
**Alien Behavior**: Aliens spawn and move downwards towards the player, with a chance to shoot back.
**Score System**: Earn points by destroying aliens; lose points if aliens reach the bottom.
**Energy System**: The player has an energy level that decreases over time.
**Game Over Condition**: The game ends when an alien collides with the player or when an alien bullet hits the player.

## Installation

To run this game, you need to have Python and Pygame installed on your computer. Follow these steps:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**: Open your command line or terminal and run:
   pip install pygame


3. **Clone the Repository**: Download the code from the repository or copy the provided code into a Python file (e.g., `space_invaders.py`).

4. **Add Assets**: Ensure the following image files are in the specified paths or adjust the code to your asset paths:
   Player Image: `D:\Desktop\2.png`
   Alien Image: `D:\Desktop\3.webp`
   Background Image: `D:\Desktop\1.webp`
   Fruit Image: `D:\Desktop\4.webp` (if used in future updates)

## Usage

Run the game by executing the Python script:
python space_invaders.py

Use the left and right arrow keys to move your player and the space bar to shoot.

## Gameplay

**Objective**: Defend against the alien invasion by shooting them before they reach the bottom of the screen.
**Scoring**: Each alien destroyed increases your score by 10 points. If an alien reaches the bottom, you lose 5 points.
**Energy**: Your energy decreases over time. Monitor your energy level displayed on the screen.
**Game Over**: The game ends if you collide with an alien or get hit by an alien bullet.

## Code Structure

**Classes**:
  Player: Handles player attributes, movement, energy, and drawing.
  Alien: Manages alien attributes, movement, shooting behavior, and drawing.
  Bullet: Represents bullets shot by the player.
  AlienBullet: Represents bullets shot by aliens.

**Game Loop**: Contains the main game logic, including event handling, updating positions, and drawing objects on the screen.

**Functions**:
create_alien(): Spawns a new alien at a random horizontal position.
game_over(): Displays a game over message (to be implemented).

## Customizations

You can customize various aspects of the game:

**Change Images**: Swap out the images used for the player, aliens, and background.
**Adjust Game Settings**: Modify constants like `ALIEN_COLUMNS`, `INITIAL_ALIEN_SPEED`, and `ALIEN_SPAWN_INTERVAL` to change game difficulty.
**Add Sounds**: Implement sound effects for shooting and explosions to enhance the experience.

## Contributing

Contributions are welcome! If you'd like to improve the game or add features, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
