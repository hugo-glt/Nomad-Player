from NomadPlayer.library import validate_library_path

def main():
    raw_input = input("Enter the path to your music library: ")
    library_path = validate_library_path(raw_input)
    print(f"Validated library path: {library_path}")


if __name__ == "__main__":
    main()

def display_music_file(mp3_files):
    for file in mp3_files:
        print(file)
