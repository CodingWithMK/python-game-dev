# 🕹️ Game Development with Python 🚀

This repository is a collection of my **Python game development journey**, documented step by step.  
The goal is to create a clean, structured, and helpful resource both for tracking my own progress and for anyone who wants to learn game development using Python.

> Main Technology: **Python** (+ optionally: [Pygame], [Pygame-ce], [arcade], etc.)  
> Package/Environment Manager: **uv**

---

## 📂 Contents

This repository includes:

- 🎮 Game projects from beginner to advanced  
  - Examples: Pong, Snake, Breakout, Tetris, Platformer, etc.
- 🧠 Game programming fundamentals  
  - Game loop, FPS management, input handling  
  - Collision detection  
  - Sprites, animations, tile maps
- 🏗️ OOP-based game architecture  
  - `Game` class, `Player`, `Enemy`, `Block`, etc.
- 🧪 Experimental demos  
  - Physics tests, simple AI movement, UI/menu systems
- 📚 Learning notes & fully commented code

---

## 🛠️ Technologies Used

- **Language:** Python `3.x`
- **Game Library:**  
  - [Pygame] / [Pygame-ce]
- **Tools:**
  - **uv** (environment + dependency manager)
  - VS Code / PyCharm  
  - Git & GitHub  

---

## 📁 Project Structure

> Example structure — adjust to your actual repository layout.

```bash
python-game-dev/
├─ README.md
├─ pyproject.toml
├─ uv.lock
├─ LICENSE
├─ docs/
│  ├─ game_loop.md
│  └─ collision_detection.md
├─ assets/
│  ├─ images/
│  ├─ sounds/
│  └─ fonts/
├─ src/
│  ├─ common/
│  │  ├─ __init__.py
│  │  ├─ settings.py
│  │  ├─ engine.py
│  │  └─ utils.py
│  ├─ games/
│  │  ├─ pong/
│  │  │  ├─ main.py
│  │  ├─ snake/
│  │  │  ├─ main.py
│  │  ├─ tetris/
│  │  │  ├─ main.py
│  │  └─ ...
│  └─ experiments/
│     ├─ physics_test.py
│     └─ particles_demo.py
└─ tests/


---

## 🚀 Installation (Using **uv**)

### 1. Clone the repository

```bash
git clone https://github.com/CodingWithMK/python-game-dev.git
cd python-game-dev
```

### 2. Create & activate an environment using **uv**

```bash
uv venv
```

Activate the environment:

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

---

### 3. Install dependencies via uv

```bash
uv sync
```

This reads `pyproject.toml` and installs everything into the uv-managed virtual environment.

---

## ▶️ Running the Games

Each game has its own entry script. For example:

### Pong

```bash
uv run src/games/pong/main.py
```

### Snake

```bash
uv run src/games/snake/main.py
```

### Tetris

```bash
uv run src/games/tetris/main.py
```

---

## 📌 Roadmap

* [x] Basic game loop prototype
* [ ] Pong
* [ ] Snake
* [ ] Tetris
* [ ] Platformer
* [ ] Highscore system
* [ ] Settings menu
* [ ] Minimal Python-based game framework

---

## 🤝 Contributing

1. Fork the repo

2. Create a new branch:

   ```bash
   git checkout -b feature/new-feature
   ```

3. Commit your changes:

   ```bash
   git commit -m "Added feature X"
   ```

4. Push the branch:

   ```bash
   git push origin feature/new-feature
   ```

5. Open a pull request 🎉

---

## 🧾 License

Choose your license, for example:

```text
MIT License
```

---

## 📬 Contact

* GitHub Issues
* Email: [musabkaya007@gmail.com](mailto:musabkaya007@gmail.com)
* LinkedIn: Muhammed Musab Kaya

---

## ⭐ Support

If this repo helped you:

* Give it a ⭐
* Share it with others who want to learn Python game development 🎮

> Game development is a long but rewarding journey — keep experimenting, keep building, and have fun!
