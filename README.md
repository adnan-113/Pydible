# Pydible
Pydible is a python machine that reads audio books by providing the correct pdf files! You can also select range of pages by selecting the pages in the main.py.
The Machine has only 12 pieces of commits with voice activity. 
The steps to initiate the .py are given bellow
1)In the line 2 of main.py { book = open('book.pdf', 'rb')} in the book.pdf, name the pdf file that u saved in the folder.
2)In the line 8 of main.py { for num in range(1, pages)} in the numerical value 1 you should give the page no. from where u wanna start. In python the numerical 0 stays as null. so to avoid the error always cut the page no:0 suppose there is a pdf file 0-8 pages, so python wont count the 0 no page, it will count from 1, so to fix the error type there 1
In the command shell, These 2 packages have to be installed

pip install pyttsx3
pip install PyPDF2
