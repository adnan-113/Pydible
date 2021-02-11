 import pyttsx3
 import PyPDF2
 book = open('book.pdf', 'rb')
 pdfReader = PyPDF2.pdfFileReader(book)
 pages = pdfReader.numPages
 print (pages)
 speaker = pyttsx3.init()
 for num in range(1, pages)
   page = pdfReader.getpage(1)
   text = page.extractText()
   speaker.say(text)
   speaker.runAndWait()