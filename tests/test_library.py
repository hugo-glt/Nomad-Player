import tempfile
import unittest
from pathlib import Path
from NomadPlayer.library import scan_audio_files, validate_library_path


class TestValidateLibraryPath(unittest.TestCase):
    def test_valid_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(validate_library_path(tmp), Path(tmp))

    def test_nonexistent_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "does_not_exist"
            with self.assertRaises(ValueError):
                validate_library_path(str(missing))

    def test_file_instead_of_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "song.mp3"
            file_path.touch()
            with self.assertRaises(ValueError):
                validate_library_path(str(file_path))


class TestScanAudioFiles(unittest.TestCase):
    def test_finds_files_recursively(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Artist" / "Album").mkdir(parents=True)
            (root / "Artist" / "Album" / "track1.mp3").touch()
            (root / "Artist" / "Album" / "track2.FLAC").touch()
            (root / "top.wav").touch()

            names = {f.name for f in scan_audio_files(root)}

            self.assertEqual(names, {"track1.mp3", "track2.FLAC", "top.wav"})

    def test_ignores_non_audio_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "notes.txt").touch()
            (root / "cover.jpg").touch()
            self.assertEqual(scan_audio_files(root), [])

    def test_ignores_directory_named_like_audio(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Live.mp3").mkdir()
            self.assertEqual(scan_audio_files(root), [])

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(scan_audio_files(Path(tmp)), [])

    def test_results_are_sorted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ["c.mp3", "a.mp3", "b.mp3"]:
                (root / name).touch()
            names = [f.name for f in scan_audio_files(root)]
            self.assertEqual(names, ["a.mp3", "b.mp3", "c.mp3"])

    def test_complex_file_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            names = ["My Song (live).mp3", "Été & Hiver.flac", "l'ami #1 [remix].ogg"]
            for name in names:
                (root / name).touch()
            found = {f.name for f in scan_audio_files(root)}
            self.assertEqual(found, set(names))


if __name__ == "__main__":
    unittest.main()