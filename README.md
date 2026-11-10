# Flappy Bird 🐤 — 2D Arcade Game in Python

![Python](https://shields.io)
![Pygame](https://shields.io)
![License](https://shields.io)
A responsive 2D recreation of the classic **Flappy Bird** arcade game built from scratch using **Python** and **Pygame**. This project demonstrates object-oriented software design, real-time 60 FPS game loop architecture, 2D physics simulation, and bounding-box collision detection.

---

## 📸 Gameplay Preview

> **Tip:** Once you upload a screenshot named `gameplay.png` to your repository, uncomment the line below by removing the `<!--` and `-->` tags!
<!-- ![Flappy Bird Gameplay](gameplay.png) -->

---

## ✨ Key Technical Highlights

* **Object-Oriented Architecture:** Encapsulates game entities into modular `Bird` and `Pipe` classes to manage state, velocity, movement, and rendering cleanly.
* **2D Physics & Collision Engine:** Implements continuous gravity acceleration (`0.25 px/frame²`), upward impulse velocity, and precise `pygame.Rect.colliderect` hitboxes for pipes and ground boundaries.
* **Procedural Obstacle Generation:** Dynamically spawns paired top and bottom pipes at timed intervals (`1500 ms`) with randomized vertical gap heights.
* **Stateful Game Loop:** Runs a locked **60 FPS** loop supporting active gameplay, real-time score tracking, game-over states, and instant keyboard-triggered restarts.
* **Remote Asset Streaming:** Fetches and decodes sprite graphics directly into memory via `urllib` and `io.BytesIO`, keeping the repository lightweight.

---

## 📂 Project Structure

```text
flappy-bird-python/
├── main.py              # Core game loop, physics, and entity classes
├── requirements.txt     # External Python dependencies
└── README.md            # Project documentation
```

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Game Framework:** Pygame
* **Standard Libraries:** `random`, `sys`, `urllib.request`, `io`

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your machine
* Active internet connection (required at launch to fetch sprite assets)

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd flappy-bird-python
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the game:**
   ```bash
   python main.py
   ```

---

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| **`SPACE`** | Flap / Jump upward during gameplay |
| **`SPACE`** | Instantly restart the game on the Game Over screen |
| **`Window Close (X)`** | Exit the application cleanly |

---

## 🔮 Future Enhancements

* [ ] Add local sprite caching in an `assets/` directory for offline play
* [ ] Integrate wing-flap, point-scoring, and collision sound effects (`pygame.mixer`)
* [ ] Implement persistent high-score tracking using JSON or SQLite
* [ ] Add animated wing-flapping frames and day/night background transitions

---

##  Acknowledgments & Credits

* Sprite graphics sourced from the open-source [FlapPyBird](https://github.com/Saurxbhh/Flappy-Bird) repository.

---

## 👨‍💻 Author

**Saurabh**  
*MCA Candidate | Uttaranchal University*  
* [GitHub](https://github.com/Saurxbhh))
