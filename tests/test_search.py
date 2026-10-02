import unittest

from ai_project.search import MazeSolver


class MazeSolverTests(unittest.TestCase):
    def test_bfs_finds_shortest_path(self):
        solver = MazeSolver([
            "########",
            "#S....##",
            "#.##.###",
            "#....G##",
            "########",
        ])

        path = solver.shortest_path_bfs()
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (1, 1))
        self.assertEqual(path[-1], (3, 5))
        self.assertEqual(len(path) - 1, 6)

    def test_astar_finds_same_path(self):
        solver = MazeSolver([
            "########",
            "#S....##",
            "#.##.###",
            "#....G##",
            "########",
        ])

        path = solver.shortest_path_astar()
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (1, 1))
        self.assertEqual(path[-1], (3, 5))
        self.assertEqual(len(path) - 1, 6)
        self.assertTrue(solver.path_to_moves(path))

    def test_unreachable_maze_returns_none(self):
        solver = MazeSolver([
            "######",
            "#S#G##",
            "######",
        ])

        self.assertIsNone(solver.shortest_path_bfs())
        self.assertIsNone(solver.shortest_path_astar())


if __name__ == "__main__":
    unittest.main()
