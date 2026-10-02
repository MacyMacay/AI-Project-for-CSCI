# AI Project for CSCI

This repository contains a small, runnable AI project for a CSCI course assignment. It demonstrates classic graph-search techniques used in artificial intelligence: breadth-first search (BFS) and A* search for solving a maze.

## Team
- mace@mail.fresnostate.edu
- asianhmongxyooj1@mail.fresnostate.edu
- ivanacs08@mail.fresnostate.edu

## Project overview
The project models a grid maze where:
- `S` marks the start
- `G` marks the goal
- `#` marks walls
- `.` marks open space

The solver uses two algorithms to find the shortest valid route:
- BFS for guaranteed shortest paths in an unweighted graph
- A* with Manhattan distance as the heuristic for efficient pathfinding

## Folder layout
- `src/ai_project/search.py` – core maze and search logic
- `src/ai_project/cli.py` – command-line runner
- `tests/test_search.py` – unit tests for correctness
- `data/example_maze.txt` – sample maze input

## Run locally
From the project root, use:

```bash
PYTHONPATH=src python -m ai_project.cli --algorithm astar --file data/example_maze.txt
```

You can also run the included tests:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Expected output
The program prints the path length and the move sequence while solving the maze. The exact move string can vary slightly depending on the search order, but the result will always be a shortest valid route.

This is a lightweight and teachable example of how search-based AI planning works in a simple environment.
