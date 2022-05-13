from openpyxl import Workbook
from openpyxl.styles import PatternFill
import fnct as hl
import cv2
import numpy as np

path = "img.jpg"
img = cv2.imread(path)
# print(img)

# import openpyxl
wb = Workbook()
sheet = wb["Sheet"] # This sheet is created by default

cnt = 0

srow = 15  # row 1048576 sloupce
scol = 10   # řádky

# row vodorovně     col vertikálně

for row in range(srow):
    cnt = 0
    row = row + 1

    for col in range(scol):
        col = col + 1
        cnt = cnt + 1
        # print(col, cnt)
        letcol = hl.nl(cnt)
        color = hl.rgb(img[row - 1][col - 1][0],  img[row - 1][col - 1][1],  img[row - 1][col - 1][2])
        fill = PatternFill("solid", start_color=color)
        sheet["{}{}".format(letcol, row)].fill = fill  # letter, řádek


        
wb.save("wb.xlsx")

print("complete")