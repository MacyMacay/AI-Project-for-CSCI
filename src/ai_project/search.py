from __future__ import annotations

from collections import deque
from heapq import heappop, heappush
from typing import Iterable

Position = tuple[int, int]


class MazeSolver:
    """Find a path through a grid maze using classic graph-search algorithms."""

    def __init__(self, grid: Iterable[str]):
        rows = tuple(line.rstrip("\n") for line in grid)
        if not rows:
            raise ValueError("Maze grid cannot be empty.")

        self.width = max(len(row) for row in rows)
        self.grid = tuple(row.ljust(self.width, "#") for row in rows)
        self.height = len(self.grid)
        self.start = self._find_marker("S")
        self.goal = self._find_marker("G")

    def _find_marker(self, marker: str) -> Position:
        for row_index, row in enumerate(self.grid):
            for col_index, char in enumerate(row):
                if char == marker:
                    return (row_index, col_index)
        raise ValueError(f"Marker '{marker}' not found in the maze.")

    def _in_bounds(self, position: Position) -> bool:
        row, col = position
        return 0 <= row < self.height and 0 <= col < self.width and self.grid[row][col] != "#"

    def _neighbors(self, position: Position) -> list[Position]:
        row, col = position
        for delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_position = (row + delta[0], col + delta[1])
            if self._in_bounds(next_position):
                yield next_position

    def shortest_path_bfs(self) -> list[Position] | None:
        queue = deque([self.start])
        came_from: dict[Position, Position | None] = {self.start: None}

        while queue:
            current = queue.popleft()
            if current == self.goal:
                return self._reconstruct_path(came_from, current)

            for neighbor in self._neighbors(current):
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    queue.append(neighbor)

        return None

    def shortest_path_astar(self) -> list[Position] | None:
        open_heap: list[tuple[int, int, Position]] = []
        came_from: dict[Position, Position | None] = {self.start: None}
        g_score: dict[Position, int] = {self.start: 0}
        f_score: dict[Position, int] = {self.start: self._heuristic(self.start, self.goal)}
        heappush(open_heap, (f_score[self.start], 0, self.start))

        while open_heap:
            _, _, current = heappop(open_heap)
            if current == self.goal:
                return self._reconstruct_path(came_from, current)

            for neighbor in self._neighbors(current):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self._heuristic(neighbor, self.goal)
                    heappush(open_heap, (f_score[neighbor], tentative_g, neighbor))

        return None

    def shortest_path(self, algorithm: str = "astar") -> list[Position] | None:
        algorithm = algorithm.lower()
        if algorithm == "bfs":
            return self.shortest_path_bfs()
        if algorithm == "astar":
            return self.shortest_path_astar()
        raise ValueError(f"Unsupported algorithm '{algorithm}'. Choose 'bfs' or 'astar'.")

    @staticmethod
    def _heuristic(position: Position, goal: Position) -> int:
        return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

    @staticmethod
    def _reconstruct_path(came_from: dict[Position, Position | None], current: Position) -> list[Position]:
        path = [current]
        while came_from[current] is not None:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def path_to_moves(self, path: Iterable[Position] | None) -> str | None:
        if path is None:
            return None

        steps = []
        positions = list(path)
        for previous, current in zip(positions, positions[1:]):
            row_delta = current[0] - previous[0]
            col_delta = current[1] - previous[1]
            if row_delta == 1:
                steps.append("D")
            elif row_delta == -1:
                steps.append("U")
            elif col_delta == 1:
                steps.append("R")
            elif col_delta == -1:
                steps.append("L")
        return "".join(steps)
