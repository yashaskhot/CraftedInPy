import requests
from gtts import gTTS

url = input(f"Enter your URL: ")

response = requests.get(url)
text = response.text

# Use gTTS to convert the text to speech
tts = gTTS(text=text, lang="en")

# Save the audio to an MP3 file
tts.save("Text to Speech/output.mp3")
