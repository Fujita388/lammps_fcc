all: fcc.lammpstrj

fcc.lammpstrj: fcc.input
	/home/Fujita388/github/lammps/src/lmp_serial < fcc.input

fcc.input: fcc.atoms

fcc.atoms: fcc.py
	python3 fcc.py


# restart.lammpstrjを作成
restart.lammpstrj: restart.input
	/home/Fujita388/github/lammps/src/lmp_serial < restart.input


# clean
clean: 
	rm *.lammpstrj *.atoms test.restart.*




