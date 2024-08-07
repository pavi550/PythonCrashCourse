# importing required modules
import PyPDF2

# creating a pdf file object
file1 = open('pythonfiles.pdf', 'rb')  #read in binary

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(file1)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(1)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
file1.close()
