# qubit number=4
# total number=19
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += H(3)  # number=2
    prog += CNOT(3,0) # number=3
    prog += Z(3) # number=14
    prog += CNOT(3,0) # number=15
    prog += RX(-2.0420352248333655,0) # number=4
    prog += CNOT(1,0) # number=5
    prog += SWAP(1,0) # number=6
    prog += CNOT(1,3) # number=7
    prog += CNOT(1,3) # number=16
    prog += CNOT(1,3) # number=17
    prog += H(2) # number=8
    prog += T(2) # number=11
    prog += T(2) # number=18
    prog += T(2) # number=12
    prog += T(2) # number=19
    prog += H(2) # number=13
    prog += CNOT(3,2) # number=9
    prog += H(2) # number=10
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

    writefile = open("startPyquil_statevector_213.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()

