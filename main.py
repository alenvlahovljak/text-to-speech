# Module for text to speech conversion
from gtts import gTTS
import os

file_name = input("Enter name of a mp3 file: ")
text_to_convert = input("Write text which you want to convert to speach: ")
language = "en"

# gTTS object to convert given text to audio file
audio_obj = gTTS(text=text_to_convert, lang=language, slow=False)
audio_obj.save(f"{file_name}.mp3")

# Play the converted audio file
os.system(f"{file_name}.mp3")
