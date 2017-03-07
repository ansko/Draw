#!/usr/bin/env python3
#coding utf-8

import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QLinearGradient, QColor, QRadialGradient
from PyQt5.QtCore import Qt

import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint

import lat
import lat.read_atoms

#----------------------
fname = '../co.50000.data'

# ionic radii
radii = [
    10,
    10,
    10,
    ]

radius = 10

masses = [
    26.9815,
    24.305,
    28.0855,
    15.9994,
    15.9994,
    15.9994,
    15.9994,
    1.00797,
    1.00797,
    12.0112,
    1.00797,
    12.0112,
    15.9994,
    14.0067,
    14.0067,
    12.0112,
    14.0067
    ]

scalex = 30
scaley = 30

lx = 0
ly = 0
lz = 0
#----------------------

class AtomsDrawer(QWidget):

    def __init__(self, atoms, sizex, sizey):

        self.atoms = atoms
        super().__init__()
        self.resize( sizex + 100, sizey  + radius)
        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):

        for atom in self.atoms:
            gradient = QRadialGradient(scalex * atom[1], scaley * atom[2], 15 * radius)
            
            if atom[0] == 1:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(255, 0, 0))
            elif atom[0] == 2:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(255, 255, 0))
            elif atom[0] == 3:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(255, 255, 255))
            elif atom[0] == 4:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(0, 255, 0))
            elif atom[0] == 5:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(0, 0, 255))
            elif atom[0] == 6:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(255, 0, 255))
            elif atom[0] == 7:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(0, 255, 255))
            elif atom[0] == 8:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(127, 127, 127))
            elif atom[0] == 9:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(255, 127, 127))
            elif atom[0] == 10:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(255, 0, 127))
            elif atom[0] == 11:
                gradient.setColorAt(0.0, QColor(0, 0, 0))
                gradient.setColorAt(0.5, QColor(255, 127, 0))

            brush = QBrush(gradient)
            qp.setBrush(brush)
            qp.drawEllipse(atom[3] * scalex, atom[2] * scaley, radius, radius)

    def screenshot(self):

        p = self.grab();
        p.save('./1.png', 'png', -1)


def main():

    cmx = 0
    cmy = 0
    cmz = 0

    [atoms, bounds, bonds, angles] = lat.read_atoms.read_atoms(fname)

    lx = bounds[1] - bounds[0]
    ly = bounds[3] - bounds[2]
    lz = bounds[5] - bounds[4]

    for atom in atoms:
        cmx += atom[4]
        cmy += atom[5]
        cmz += atom[6]
        atom.pop(9)
        atom.pop(8)
        atom.pop(7)
        atom.pop(3)
        atom.pop(1)
        atom.pop(0)

    cmx /= len(atoms)
    cmy /= len(atoms)
    cmz /= len(atoms)

    for atom in atoms:
        atom[1] -= cmx
        atom[2] -= cmy
        atom[3] -= cmz
        atom[1] += lx / 2
        atom[2] += ly / 2
        atom[3] += lz / 2

    sizex = int(scalex * lz)
    sizey = int(scaley * ly)

    app = QApplication(sys.argv)
    ad = AtomsDrawer(atoms, sizex, sizey)
    ad.screenshot()
    sys.exit(app.exec_())

    return None

main()
