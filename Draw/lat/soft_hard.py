# encoding utf-8

def soft_hard(number, atom):
    atom_charge = atom[3]

    if (atom_charge in [1.575, 1.36, 2.1, -1.05, -0.95, -1.1688, -1.0808, 0.4245]):
        return 1
    else:
        return 2
