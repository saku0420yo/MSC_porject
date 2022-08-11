# qubit number=4
# total number=28
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += H(0) # number=2
    prog += CZ(2,0) # number=23
    prog += H(0) # number=24
    prog += Z(2) # number=13
    prog += CNOT(2,0) # number=14
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += CNOT(3,0) # number=10
    prog += CNOT(3,0) # number=15
    prog += Z(3) # number=25
    prog += CNOT(3,0) # number=26
    prog += CNOT(3,0) # number=16
    prog += CNOT(1,0) # number=5
    prog += SWAP(2,3) # number=6
    prog += SWAP(3,1) # number=12
    prog += H(2) # number=7
    prog += S(2) # number=17
    prog += T(2) # number=18
    prog += T(2) # number=27
    prog += H(2) # number=19
    prog += CNOT(3,2) # number=9
    prog += Z(3) # number=11
    prog += H(2) # number=8
    prog += T(2) # number=20
    prog += T(2) # number=28
    prog += S(2) # number=21
    prog += H(2) # number=22
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

    writefile = open("startPyquil_statevector_217.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()

