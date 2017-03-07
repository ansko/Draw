# encoding utf-8

def read_atoms(filename):
    """Прочитать датафайл и вернуть атомы и границы в списке
       To read datafile and return atoms and bond in the list"""
    f = open(filename, 'r')
    flag = 0
    atoms = []
    bonds = []
    angles = []
    bounds = []

    atom = 0
    bond = 0
    angle = 0

    for line in f:
        if line.endswith('xlo xhi\n'):
            line_s = line.split()
            bounds.append(float(line_s[0]))
            bounds.append(float(line_s[1]))
        if line.endswith('ylo yhi\n'):
            line_s = line.split()
            bounds.append(float(line_s[0]))
            bounds.append(float(line_s[1]))
        if line.endswith('zlo zhi\n'):
            line_s = line.split()
            bounds.append(float(line_s[0]))
            bounds.append(float(line_s[1]))
        if line.startswith('Atoms # full'):
            flag = 1
            continue
        if line.startswith('Velocities'):
            flag = 0

        if line.startswith('Bonds'):
            flag = 2
            continue

        if line.startswith('Angles'):
            flag = 3
            continue

        if line.startswith('Dihedrals'):
            flag = 3
            break

        if flag == 1:
            line = line.split()
            atoms.append([])
            for word in line:
                try:
                    word = int(word)
                except:
                    word = float(word)
                atoms[atom].append(word)
            atom += 1

        if flag == 2:
            line = line.split()
            bonds.append([])
            for word in line:
                try:
                    word = int(word)
                except:
                    word = float(word)
                bonds[bond].append(word)
            bond += 1

        if flag == 3:
            line = line.split()
            angles.append([])
            for word in line:
                try:
                    word = int(word)
                except:
                    word = float(word)
                angles[angle].append(word)
            angle += 1

    atoms.pop(0)
    atoms.pop(len(atoms) - 1)
    atoms.sort()

    bonds.pop(0)
    bonds.pop(len(bonds) - 1)
    bonds.sort()

    angles.pop(0)
    angles.pop(len(angles) - 1)
    angles.sort()

    return (atoms, bounds, bonds, angles)
