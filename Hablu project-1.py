
from  PyPDF2 import PdfMerger
AllPDF=["1.pdf.pdf","2.pdf.pdf"]
x= PdfMerger()
for newpdf in AllPDF:
    x.append(newpdf)

x.write("Hablu.pdf")
x.close()




