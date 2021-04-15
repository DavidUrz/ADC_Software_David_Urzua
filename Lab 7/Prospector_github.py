import os

clone = "git clone https://github.com/DavidUrz/ADC_Software_David_Urzua.git"
path = os.getcwd()

os.system("cd " + path)
# os.system(clone)
os.system("prospector --o text:report_prospector_fixed.txt")