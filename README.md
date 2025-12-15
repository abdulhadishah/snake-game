# 🐍 Snake Game

A classic Snake game built using Python Turtle Graphics. The snake moves smoothly across the screen, grows when it eats food, and can be played in two modes: a standard game-over version and an upgraded version with a persistent high score.

## ✨ Technologies

- `Python`
- `Turtle Graphics`
- `Time`
- `File Handling`

## 🚀 Features

- Smooth snake movement with keyboard controls
- Food spawning at random locations
- Boundary and self-collision detection
- Classic game-over version
- Persistent high score version using file storage
- Clean, dark-themed UI with visual boundaries

## 📍 The Process

This project was developed across **Day 20, Day 21, and Day 24 of the 100 Days of Python Code** course.

On **Day 20**, the focus was on understanding how snake movement works by updating body segments in reverse order using the `range` function. Each segment follows the one ahead of it by copying its x and y coordinates, while the head moves independently.

On **Day 21**, the game logic was structured using multiple classes. This reinforced concepts like constructors (`__init__`), class inheritance, slicing lists and tuples, and managing object state for the snake, food, scoreboard, and boundaries.

On **Day 24**, file handling was introduced to persist data across game sessions. The game was upgraded to store and read a high score from a file using different file modes and paths. When the snake collides with a wall or itself, the current score resets while the highest score achieved is saved and displayed.

## 🚦 Running the Project

1. Clone the repository  
2. Run the main file: `python main.py`  
3. Control the snake using arrow keys or WASD  
4. Try to beat the stored high score  
5. Click anywhere to exit

## 🎞️ Preview

**Before (without high score):**  
https://github.com/user-attachments/assets/9c6e19cb-6a3e-4d0c-8887-5b3887ee627c


**After (with high score system):**  
https://github.com/user-attachments/assets/d9a9f77d-5afc-4c94-8973-9409af26fb7c





