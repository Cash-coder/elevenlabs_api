import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from elevenlabs import save

load_dotenv()  # load .env file

def get_text():
  base_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(base_dir, 'text_to_convert.txt')

  with open(file_path, "r", encoding="utf-8") as f:
    return f.read()    


filename = input("enter download file name ")
print("creating audio output")

client = ElevenLabs(
    # base_url="https://api.elevenlabs.io"
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = client.text_to_speech.convert(
    text=get_text(),
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    # model_id="eleven_multilingual_v2",
    model_id="eleven_flash_v2.5",
    output_format="mp3_44100_128",
    # voice_id="JBFqnCBsd6RMkjVDRZzb",
)

# play(audio)
save(audio, filename.strip() + '.mp3')
