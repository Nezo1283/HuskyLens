import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import os
import json
# import HuskyTEST2

os.chdir(os.path.dirname(__file__))

CONST_PROPORTION = 4

wb = load_workbook(filename = 'PositionXYZ.xlsx')
sheet_ranges = wb['ValueDeplacement']
lenListe = 0

for i in sheet_ranges.values:
    lenListe += 1

print(lenListe)
i = 0
listeX = []
listeY = []
listeZ = []
while i < lenListe:
    i += 1
    listeX.append(sheet_ranges[f'A{i}'].value)
    listeY.append(sheet_ranges[f'B{i}'].value)
    listeZ.append(sheet_ranges[f'C{i}'].value)
print(listeX)
print(listeY)
print(listeZ)

plt.rcParams['legend.fontsize'] = 10


fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')

# ax = fig.gca(projection='3d')

ax.plot(listeX[1:], listeY[1:], listeZ[1:], label='3D déplacement TAG')
ax.set_xlabel(listeX[0])
ax.set_ylabel(listeY[0])
ax.set_zlabel(listeZ[0])
ax.set_ylim(240*CONST_PROPORTION, 0)
ax.set_xlim(0, 320*CONST_PROPORTION)
ax.legend()

bx = fig.add_subplot(1, 2, 2)
bx.plot(listeX[1:], listeY[1:], label='2D déplacement TAG')
bx.set_xlabel(listeX[0])
bx.set_ylabel(listeY[0])
bx.set_ylim(240*CONST_PROPORTION, 0)
bx.set_xlim(0, 320*CONST_PROPORTION)
bx.grid(True)

bx.legend()

plt.show()