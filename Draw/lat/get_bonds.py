# encoding utf-8

import math

import lat.read_atoms

def get_bonds(filename):
    (atoms, bounds, bonds, angles) = lat.read_atoms.read_atoms(filename)
    bondsnumber = len(bonds)
    bondsvector = []
    for i in range(bondsnumber):
        atom1 = atoms[bonds[i][2] - 1]
        atom2 = atoms[bonds[i][3] - 1]
        bondtype = bonds[i][1]
        #x
        bondx1 = atom2[4] - atom1[4]
        bondx2 = bounds[1] - bounds[0] - abs(bondx1)
        if abs(bondx1) < abs(bondx2):
            bondx = bondx1
        else:
            bondx = -math.copysign(bondx2, bondx1)
        #y
        bondy1 = atom2[5] - atom1[5]
        bondy2 = bounds[3] - bounds[2] - abs(bondy1)
        if abs(bondy1) < abs(bondy2):
            bondy = bondy1
        else:
            bondy = -math.copysign(bondy2, bondy1)
        #z
        bondz1 = atom2[6] - atom1[6]
        bondz2 = bounds[5] - bounds[4] - abs(bondz1)
        if abs(bondz1) < abs(bondz2):
            bondz = bondz1
        else:
            bondz = -math.copysign(bondz2, bondz1)

        bond2 = bondx**2 + bondy**2 + bondz**2
        bondsvector.append([bondx, bondy, bondz])
        if bond2 > 5:
            print("x :", bondx1, bondx2, bondx);
            print("y :", bondy1, bondy2, bondy);
            print("z :", atom1[6], atom2[6], bondz1, bondz2, bondz);
            print(bonds[i][0], bondtype, bond2)
            return None

    return bondsvector
