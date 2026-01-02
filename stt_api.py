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
print("creating audio output ... ")

client = ElevenLabs(
  # base_url="https://api.elevenlabs.io"
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = client.text_to_speech.convert(
    text=get_text(),
    # voice_id="N2lVS1w4EtoT3dr4eOWO", #w40k
    voice_id="EiNlNiXeDU1pqqOPrYMO",
    # model_id="eleven_multilingual_v2",
    model_id="eleven_flash_v2_5",
    output_format="mp3_44100_128",
)

# play(audio)
save(audio, 'results/' + filename.strip() + '.mp3')

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

