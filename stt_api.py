import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
import io

load_dotenv()  # load .env file

# Sound file paths (easily configurable)
INTRO_SOUND = "sounds/zapsplat_bells_bell_large_ring_designed_105683.mp3"
OUTRO_SOUND = "sounds/zapsplat_bells_bell_large_ring_designed_105683.mp3"
INTRO_PAUSE_SECONDS = 3  # Pause after intro sound
OUTRO_PAUSE_SECONDS = 0.7  # Pause before outro sound

def get_quotes():
		"""Read and split text file into individual quotes (separated by blank lines)"""
		base_dir = os.path.dirname(os.path.abspath(__file__))
		file_path = os.path.join(base_dir, 'text_to_convert.txt')

		with open(file_path, "r", encoding="utf-8") as f:
			content = f.read()
		# Split by blank lines and filter out empty strings
		quotes = [q.strip() for q in content.split('\n\n') if q.strip()]
		return quotes


filename = input("enter download file name: ")
pause_duration = int(input("enter pause duration in seconds (e.g., 6): "))

print(f"creating audio output with {pause_duration}s pauses... ")

client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

quotes = get_quotes()
print(f"Found {len(quotes)} quotes to process")

# Load intro and outro sounds
print("Loading intro and outro sounds...")
intro_sound = AudioSegment.from_file(INTRO_SOUND)
outro_sound = AudioSegment.from_file(OUTRO_SOUND)

# Generate audio for each quote
audio_segments = []
for i, quote in enumerate(quotes, 1):
  print(f"Generating audio for quote {i}/{len(quotes)}...")

  audio_bytes = client.text_to_speech.convert(
    text=quote,
    voice_id="EiNlNiXeDU1pqqOPrYMO",
    model_id="eleven_flash_v2_5",
    output_format="mp3_44100_128",
  )

  # Convert generator to bytes
  audio_data = b''.join(audio_bytes)

  # Load as AudioSegment
  audio_segment = AudioSegment.from_mp3(io.BytesIO(audio_data))
  audio_segments.append(audio_segment)

# Create silence segments (in milliseconds)
silence_between_quotes = AudioSegment.silent(duration=pause_duration * 1000)
silence_after_intro = AudioSegment.silent(duration=INTRO_PAUSE_SECONDS * 1000)
silence_before_outro = AudioSegment.silent(duration=OUTRO_PAUSE_SECONDS * 1000)

# Build final audio: for each quote: intro -> 3s -> quote -> 0.7s -> outro -> [pause] -> next quote
print("Concatenating audio segments with pauses...")
final_audio = AudioSegment.empty()

for i, segment in enumerate(audio_segments):
  # Add intro sound + pause before quote
  final_audio += intro_sound + silence_after_intro

  # Add the quote
  final_audio += segment

  # Add pause + outro sound after quote
  final_audio += silence_before_outro + outro_sound

  # Add pause between quotes (except after last quote)
  if i < len(audio_segments) - 1:
    final_audio += silence_between_quotes

# Export the final audio
output_path = f'results/{filename.strip()}.mp3'
final_audio.export(output_path, format="mp3")
print(f"Audio saved to {output_path}")

# print credits used
# import requests

# def print_last_query_credits(api_key):
#     headers = {"xi-api-key": api_key}
#     response = requests.get("https://api.elevenlabs.io/v1/user/subscription", headers=headers)
    
#     if response.status_code == 200:
#         data = response.json()
#         print(f"Credits used: {data.get('character_count', 'N/A')}/{data.get('character_limit', 'N/A')}")
#     else:
#         print(f"Error: {response.status_code}")

# # Usage
# api_key = "your_api_key_here"
# print_last_query_credits(api_key)

