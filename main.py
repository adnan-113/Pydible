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

print(f"Number of Pages in the PDF: {pages}")



# speaker = pyttsx3.init()

page_number = int(input("Enter the number of the page that you want to read: "))

page = pdfReader.getPage(page_number)
text = page.extractText()
print(text)

"""
for num in range(1, pages):
  page = pdfReader.getPage(page_number)
  text = page.extractText()
  print(text)
  # speaker.say(text)
  # speaker.runAndWait()

"""