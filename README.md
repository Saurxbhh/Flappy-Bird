# 🐤 Flappy Bird Clone in Python

A classic 2D arcade clone of **Flappy Bird** built using Python and **Pygame**. This project demonstrates object-oriented game architecture, 60 FPS game loops, gravity physics, and bounding-box collision detection.

## ✨ Features
* **Object-Oriented Design:** Modular `Bird` and `Pipe` classes for clean state management and rendering.
* **2D Physics & Collisions:** Smooth gravity acceleration, jump velocity mechanics, and accurate `colliderect` hitboxes.
* **Dynamic Obstacles:** Procedural pipe generation with randomized vertical gaps and real-time score tracking.
* **Instant Restart:** Press `SPACE` on the Game Over screen to reset and play again immediately.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Library:** Pygame

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd flappy-bird-python
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```
   *(Note: An active internet connection is required on startup to fetch sprite assets.)*

## 🎮 Controls
* **SPACEBAR:** Flap / Jump (and restart after Game Over)

## 🙏 Credits
* Sprite assets sourced from the open-source [FlapPyBird](https://github.com) repository.
