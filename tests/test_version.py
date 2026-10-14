import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import server


class TestServerVersion(unittest.TestCase):
    def test_version_flag_prints_version_and_exits(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            board_file = os.path.join(tmpdir, "board.json")
            env = dict(os.environ)
            env["DEV_ROOM_DATA"] = board_file

            result = subprocess.run(
                [sys.executable, os.path.join(ROOT, "server.py"), "--version"],
                capture_output=True,
                text=True,
                env=env,
            )

            self.assertEqual(result.returncode, 0)
            self.assertIn(server.VERSION, result.stdout.strip())
            self.assertIn("dev-room", result.stdout.strip())
            self.assertFalse(os.path.exists(board_file), "board.json must not be created on --version")

    def test_version_short_flag(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            board_file = os.path.join(tmpdir, "board.json")
            env = dict(os.environ)
            env["DEV_ROOM_DATA"] = board_file

            result = subprocess.run(
                [sys.executable, os.path.join(ROOT, "server.py"), "-v"],
                capture_output=True,
                text=True,
                env=env,
            )

            self.assertEqual(result.returncode, 0)
            self.assertIn(server.VERSION, result.stdout.strip())
            self.assertFalse(os.path.exists(board_file))


if __name__ == "__main__":
    unittest.main()
