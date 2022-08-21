from googletrans import Translator

translator = Translator()

text ="ich bin ein programmmer"
translation = translator.translate(text, src="de", dest="en")

print(translation.text)