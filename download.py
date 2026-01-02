from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.history.download(
    history_item_ids=[
        "a1b2c3d4-e5f6-7890-ab12-cd34ef567890"
    ],
    output_format="wav"
)
