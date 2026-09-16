# NOMAD PLAYER

NOMAD PLAYER (NPlayer) is a minimalist music for terminal in Python

The goal of this project is to provide a portable, installable music player that can run on a wide range of devices and play music files directly from files provided by the user.

In the future, the application will also be distributed as standalone executables, allowing for maximum portability across different devices and environments. The ultimate goal is to make the application usable anywhere, for example, by running it directly from a USB drive without requiring a traditional installation.

## INSTALLATION (dev)

```
    python -m venv venv
    venv\Scripts\activate
    pip install -e .
```

## STRUCTURE

```
Nplayer/
├── .git/
├── .gitignore
├── .venv/
├── pyproject.toml
├── README.md
├── src/
│ ├── NomadPlayer/
│ │ ├── __init__.py
│ │ ├── cli.py
│ │ ├── library.py
│ │ └── player.py
│ └── nplayer.egg-info/
│ ├── dependency_links.txt
│ ├── entry_points.txt
│ ├── PKG-INFO
│ ├── SOURCES.txt
│ └── top_level.txt
└── tests/
├── __init__.py
└── test_library.py
```