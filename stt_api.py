import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from elevenlabs import save


def get_text():
  base_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(base_dir, 'text_to_convert.txt')

  with open(file_path, "r", encoding="utf-8") as f:
    return f.read()    

text = get_text()
filename = input("enter download file name ")

audio = elevenlabs.text_to_speech.convert(
    text=text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

# play(audio)
save(audio, filename.strip() + '.mp3')
