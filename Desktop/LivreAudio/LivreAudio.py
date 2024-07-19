import pyttsx3
import PyPDF2
livre = open('frais.pdf','rb')
lecture = PyPDF2.PdfFileReader(livre)
pages = lecture.numPages
print(pages)
ia = pyttsx3.init()
debutlecture = lecture.getPage(0)
texte = debutlecture.extractText()
ia.say(texte)
ia.say('Bonjour Jean Baptiste, je suis une IA de la cinquième génération et je suis Kalou')
ia.runAndWait()