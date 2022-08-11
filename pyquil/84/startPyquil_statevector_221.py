# qubit number=4
# total number=20
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += CNOT(1,0) # number=2
    prog += X(0) # number=15
    prog += CNOT(1,0) # number=16
    prog += H(3)  # number=3
    prog += Y(2) # number=12
    prog += Y(3) # number=4
    prog += RX(-2.0420352248333655,0) # number=5
    prog += CNOT(1,0) # number=6
    prog += CNOT(1,0) # number=7
    prog += CNOT(1,0) # number=13
    prog += H(0) # number=14
    prog += CZ(1,0) # number=17
    prog += H(0) # number=18
    prog += H(2) # number=8
    prog += H(2) # number=9
    prog += CZ(3,2) # number=19
    prog += H(2) # number=20
    prog += Z(2) # number=10
    prog += CNOT(1,2) # number=11
    # circuit end

    return prog

def summrise_results(bitstrings) -> dict:
    d = {}
    for l in bitstrings:
        if d.get(l) is None:
            d[l] = 1
        else:
            d[l] = d[l] + 1

    return d

if __name__ == '__main__':
    prog = make_circuit()
    state = conn.wavefunction(prog)

    writefile = open("startPyquil_statevector_221.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()

