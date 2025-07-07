"""
create_video.py – Skapar en färdig TikTok-video.
Bygger upp en video med bild + voiceover för varje scen.
Använder MoviePy. Läggs ev. till bakgrundsmusik.
Sparas som en mp4 i assets/output/.
"""

from moviepy.editor import *
import os

def create_final_video(image_paths, audio_paths, music_path, project_id):
    clips = []

    for img_path, audio_path in zip(image_paths, audio_paths):
        try:
            # Ladda ljudklippet
            audio_clip = AudioFileClip(audio_path)
            duration = float(audio_clip.duration)

            # Ladda bild
            img_clip_raw = ImageClip(img_path, duration=duration)

            # Kontrollera storlek
            min_side = min(img_clip_raw.w, img_clip_raw.h)

            # Skapa Ken Burns-effekt med säker beskärning
            img_clip = (
                img_clip_raw
                .resize(height=1080)
                .crop(width=min_side, height=min_side, x_center=img_clip_raw.w / 2, y_center=img_clip_raw.h / 2)
                .resize(lambda t: 1 + 0.01 * t)
                .set_audio(audio_clip)
            )

            clips.append(img_clip)

        except Exception as e:
            print(f"Error processing scene: {e}")

    if not clips:
        print("No scenes to compile.")
        return

    # Kombinera alla scenklipp
    final_video = concatenate_videoclips(clips, method="compose")

    # Lägg till musik om tillgänglig
    if music_path:
        try:
            background_music = AudioFileClip(music_path).volumex(0.2)
            final_audio = CompositeAudioClip([final_video.audio, background_music])
            final_video = final_video.set_audio(final_audio)
        except Exception as e:
            print(f"Failed to add music: {e}")

    # Exportera video
    output_path = os.path.join("assets/output", f"{project_id}.mp4")
    final_video.write_videofile(output_path, fps=30, codec="libx264", audio_codec="aac")
    print(f"✅ Video saved to: {output_path}")
