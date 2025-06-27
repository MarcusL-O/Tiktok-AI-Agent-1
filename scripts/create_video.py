from moviepy.editor import ImageClip, AudioFileClip

def create_video(image_path, audio_path, output_path="assets/output/final.mp4"):
    image_clip = ImageClip(image_path).set_duration(AudioFileClip(audio_path).duration)
    image_clip = image_clip.resize(height=1920).set_position("center")

    audio_clip = AudioFileClip(audio_path)

    final_clip = image_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, fps=24)

    print("✅ Video skapad:", output_path)
