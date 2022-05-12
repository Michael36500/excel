from openpyxl import Workbook
from openpyxl.styles import PatternFill
import fnct as hl
import cv2
import numpy as np

path = "img.jpg"
img = cv2.imread(path, 0)
print(img)


# import openpyxl
wb = Workbook()
sheet = wb["Sheet"] # This sheet is created by default

cnt = 0

# projede všechny sloupce
for row in img:
    cnt = cnt + 1
    letline = hl.nl(cnt)

    # projede sloupec po řádkách
    for linew in row:
        # row = row + 1
        print(row)
        color = hl.rgb(row,row,row)
        fill = PatternFill("solid", start_color=color)
        sheet["{}{}".format(letline, row)].fill = fill


wb.save("wb.xlsx")

print("complete")