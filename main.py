from scripts.generate_script import generate_script
from scripts.text_to_speech import text_to_speech
from scripts.create_video import create_video

ämne = "Vad händer om solen slocknar?"
manus = generate_script(ämne)
print(manus)

text_to_speech(manus)
create_video("assets/images/test.png", "assets/audio/output.mp3")
