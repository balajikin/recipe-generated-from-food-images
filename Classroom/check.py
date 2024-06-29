from googletrans import Translator

translator = Translator()
msg = "what can i do?"  # Your message to be translated
output = translator.translate(msg, dest='ta').text

print(output)  # Output will contain the translated text
