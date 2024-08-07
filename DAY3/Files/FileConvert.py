import win32com.client
def convert_file(excel_file,pdf_file):
    excel = win32com.client.Dispatch("Excel.Application")
    openfile = excel.workbooks.open(excel_file)
    openfile.ExportAsFixedFormat(0,pdf_file)
    print("File converted Successfully..")
    openfile.Close(False) excel.Quit()
    excel_file = r'C:\Users\Namish\Desktop\Python_Aug24\Cloud TOC AWS,Azure&GCP.xlsx'
    pdf_file = r'C:\Users\Namish\Desktop\Python_Aug24\output.pdf' convert_file(excel_file,pdf_file)