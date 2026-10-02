from __future__ import annotations

import argparse
from pathlib import Path

from ai_project.search import MazeSolver

DEFAULT_MAZE = [
    "########",
    "#S....#",
    "#.##.#",
    "#....G#",
    "########",
]


def load_maze(path: str | None) -> list[str]:
    if path:
        return Path(path).read_text().splitlines()
    return DEFAULT_MAZE


def main() -> None:
    parser = argparse.ArgumentParser(description="Solve a maze using BFS or A*.")
    parser.add_argument("--file", type=str, help="Path to a maze file. Each row is one line of the maze.")
    parser.add_argument("--algorithm", choices=["bfs", "astar"], default="astar", help="Search algorithm to use.")
    args = parser.parse_args()

    grid = load_maze(args.file)
    solver = MazeSolver(grid)
    path = solver.shortest_path(args.algorithm)
    moves = solver.path_to_moves(path)

    if path is None:
        print("No path found.")
        raise SystemExit(1)

    print(f"Path length: {len(path) - 1}")
    print(f"Moves: {moves}")
    print(f"Visited positions: {len(path)}")


if __name__ == "__main__":
    main()
