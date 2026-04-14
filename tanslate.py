from googletrans import Translator
text = "Hi, how are you doing today?"
translator = Translator()
translated = translator.translate(text, src='en',dest='ta')
print("Tamil Translation:", translated.text)

#pip install googletrans==4.0.0rc1
