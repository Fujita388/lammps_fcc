import numpy as np


class Atom:
    def __init__(self, x, y, z, xvel):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        self.vx = xvel
        self.vy = 0.0
        self.vz = 0.0


#密度から格子数を計算　L: シミュレーションボックス　rho: 密度
def get_lattice_number(L, rho):
	m = np.floor((L**3 * rho / 4.0)**(1.0 / 3.0))
	drho1 = np.abs(4.0 * m **3 / L**3 - rho)
	drho2 = np.abs(4.0 * (m + 1)**3 / L**3 - rho)
	if drho1 < drho2:
		return m
	else:
		return m + 1


def add_ball(atoms, xpos, xvel, L, rho):
	m = int(get_lattice_number(L, rho))  #格子数
	s = 2.0     #単位格子の一辺の長さ
	h = 0.5 * s
	for ix in range(0, m):   #原子数は8倍になる
		for iy in range(0, m):
			for iz in range(0, m):
				x = ix * s
				y = iy * s
				z = iz * s
				atoms.append(Atom(x, y, z, xvel))
				atoms.append(Atom(x, y+h, z+h, xvel))
				atoms.append(Atom(x+h, y, z+h, xvel))
				atoms.append(Atom(x+h, y+h, z, xvel))


def save_file(filename, atoms):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write("0.00 20.00 xlo xhi\n")
        f.write("0.00 20.00 ylo yhi\n")
        f.write("0.00 20.00 zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
    print("Generated {}".format(filename))


atoms = []

add_ball(atoms, 0.0, 0.0, 20, 0.5)

save_file("fcc.atoms", atoms)
