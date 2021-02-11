import pyttsx3
import PyPDF2

# Get the name of the book 
book_name= input("Enter the name of the pdf: ")

# Open the book
book = open(book_name, 'rb')

# read the book
pdfReader = PyPDF2.PdfFileReader(book)

# get the number of pages
pages = pdfReader.numPages

print(pages)


# # initlialize the pyttsx3 module
# speaker = pyttsx3.init()

for num in range(1, pages):
  page = pdfReader.getPage(1)
  text = page.extractText()
  print(text)
  # speaker.say(text)
  # speaker.runAndWait()