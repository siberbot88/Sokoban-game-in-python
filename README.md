Berikut adalah contoh file `README.md` untuk proyek game Sokoban yang Anda buat menggunakan Python dan Pygame:

---

# Sokoban Game in Python

![Sokoban Screenshot](![Screenshot 2025-02-02 142754](https://github.com/user-attachments/assets/3f9cf6bd-3342-4e2e-a775-efef82786ecb)
) <!-- Add a screenshot if available -->

A simple implementation of the classic Sokoban puzzle game using Python and Pygame. The goal of the game is to push all the boxes onto the designated storage locations.

---

## Features

- Classic Sokoban gameplay mechanics.
- Simple and clean graphics.
- Customizable levels.
- Victory detection when all boxes are placed correctly.

---

## Requirements

To run this game, you need the following:

- Python 3.x
- Pygame library

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sokoban-python.git
   cd sokoban-python
   ```

2. **Install Pygame**:
   If you don't have Pygame installed, you can install it using pip:
   ```bash
   pip install pygame
   ```

3. **Run the game**:
   ```bash
   python sokoban.py
   ```

---

## How to Play

- Use the **arrow keys** to move the player.
- Push the boxes onto the red circles (storage locations).
- The game will display "VICTORY!" when all boxes are correctly placed.

---

## Customizing Levels

You can create your own levels by modifying the `level_data` array in the `sokoban.py` file. Here's how the symbols work:

- `#`: Wall
- `.`: Storage location
- `@`: Player
- `$`: Box
- `*`: Box on a storage location
- `+`: Player on a storage location

Example level:
```python
level_data = [
    "###########",
    "#    #    #",
    "#   .$.  .#",
    "#    @  ###",
    "###########",
]
```

---

## Code Structure

- **`sokoban.py`**: The main game script containing the game logic, rendering, and level parsing.
- **`README.md`**: This file, providing an overview of the project.

---

## Contributing

Contributions are welcome! If you'd like to improve the game, feel free to:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by the classic Sokoban game.
- Built using the Pygame library.

---

Enjoy playing Sokoban! 🎮
