from NomadPlayer.library import scan_audio_files, validate_library_path


def display_music_file(audio_files):
    for file in audio_files:
        print(file)

def main():
    raw_input = input("Enter the path to your music library: ")
    library_path = validate_library_path(raw_input)
    audio_files = scan_audio_files(library_path)
    print(f"Found {len(audio_files)} audio files.")
    display_music_file(audio_files)

if __name__ == "__main__":
    main()
