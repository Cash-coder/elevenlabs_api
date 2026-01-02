import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
    base_url="https://api.elevenlabs.io"
)

print(client.history.list())
