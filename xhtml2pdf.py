from xhtml2pdf import pisa
import os

with open("test_template.html", "r", encoding='utf-8') as f:
        source_html= f.read()

with open("test.pdf", "w+b") as f:
        pisa_status = pisa.CreatePDF(source_html, dest=f)

os.system("test.pdf")
