# importing required modules
import PyPDF2

# creating a pdf file object
file1 = open('pythonfiles.pdf', 'rb')  #read in binary

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(file1)

# printing number of pages in pdf file
print(len(pdfReader.pages))

# creating a page object
pageObj = pdfReader.pages[1]

# extracting text from page
print(pageObj.extract_text())

# closing the pdf file object
file1.close()
