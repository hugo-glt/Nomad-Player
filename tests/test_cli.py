import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from NomadPlayer.cli import display_music_file, main


class TestDisplayMusicFile(unittest.TestCase):
    def test_prints_one_file_per_line(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            display_music_file([Path("a.mp3"), Path("b.flac")])
        self.assertEqual(buffer.getvalue().splitlines(), ["a.mp3", "b.flac"])

    def test_prints_nothing_for_empty_list(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            display_music_file([])
        self.assertEqual(buffer.getvalue(), "")


class TestMain(unittest.TestCase):
    def test_lists_only_audio_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "a.mp3").touch()
            (Path(tmp) / "b.txt").touch()

            buffer = io.StringIO()
            with patch("builtins.input", return_value=tmp), redirect_stdout(buffer):
                main()
            output = buffer.getvalue()

        self.assertIn("Found 1 audio files.", output)
        self.assertIn("a.mp3", output)
        self.assertNotIn("b.txt", output)

    def test_invalid_path_raises_value_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = str(Path(tmp) / "nope")
        with patch("builtins.input", return_value=missing):
            with self.assertRaises(ValueError):
                main()


if __name__ == "__main__":
    unittest.main()