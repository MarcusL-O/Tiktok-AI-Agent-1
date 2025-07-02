"""
select_music.py – Ger användaren val att välja bakgrundsmusik manuellt
eller hoppa över helt. Hämtar .mp3 från assets/music/.
"""

import os

def select_background_music(project_id):
    music_folder = "assets/music"
    if not os.path.exists(music_folder):
        print("No music folder found.")
        return None

    music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    if not music_files:
        print("No music files available.")
        return None

    print("\n🎵 Available music:")
    for i, file in enumerate(music_files):
        print(f"{i+1}. {file}")
    print("0. No music")

    choice = input("Select music number (or 0 for no music): ").strip()

    if choice == "0":
        return None

    try:
        index = int(choice) - 1
        selected = music_files[index]
        path = os.path.join(music_folder, selected)
        print(f"Music selected: {selected}")
        return path
    except (ValueError, IndexError):
        print("Invalid selection. No music will be used.")
        return None
