from gtts import gTTS
text = "Hi, how are you?"
tts = gTTS(text=text)
tts.save("Sample.mp3")
print("output saved as audio.mp3")