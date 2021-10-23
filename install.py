import os, sys, platform
os.system("pip install pypdf2")
os.system("pip install PyPDF2")
os.system("clear")

if os.name == "Linux":
  os.system("python3 Pdfencrypt.py")
else:
  os.system("python Pdfencrypt.py")
