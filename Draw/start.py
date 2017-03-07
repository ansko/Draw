#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QLinearGradient, QColor, QRadialGradient
from PyQt5.QtCore import Qt

radius = 3
atoms = [[]]

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):
        #print(atoms[0])

        for atom in atoms:
            gradient = QRadialGradient(atom[1], atom[2], 15 * radius)
            gradient.setColorAt(0.0, QColor(0, 0, 0))
            gradient.setColorAt(0.5, QColor(255, 0, 0))
            brush = QBrush(gradient)
            qp.setBrush(brush)
            qp.drawEllipse(2 * atom[3], 5 * atom[2], radius, radius)

    def screenshot(self):
        p = self.grab();
        p.save('./1.png', 'png', -1)

def read_atoms():
    f = open('co.50000.data', 'r')
    start=0

    for i in range(1, 31158 + 1):
        atoms.append([0, 0, 0, 0])

    i = 0

    for line in f:
        i += 1
        if line.startswith("Atoms"):	#start reading here
            start = i + 1
        if line.startswith("Velocities"): # finsih reading here
            break
        if i > start > 0:
            line_splitted = line.split()
            if len(line_splitted) == 0:
                continue
            atoms[int(line_splitted[0])] = [float(line_splitted[2]), # type 
                                            float(line_splitted[4]), # x
                                            float(line_splitted[5]), # y
                                            float(line_splitted[6])] # z
    atoms.pop(0)
    return atoms


if __name__ == '__main__':
    read_atoms()
    app = QApplication(sys.argv)
    ex = Example()
    ex.screenshot()
    sys.exit(app.exec_())
