# qubit number=4
# total number=51
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += T(2) # number=2
    prog += T(2) # number=35
    prog += S(2) # number=11
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += T(3) # number=10
    prog += T(3) # number=43
    prog += S(3) # number=36
    prog += H(1) # number=5
    prog += H(1) # number=17
    prog += H(1) # number=24
    prog += CZ(2,1) # number=44
    prog += H(1) # number=45
    prog += H(1) # number=25
    prog += H(1) # number=18
    prog += H(0) # number=6
    prog += H(0) # number=19
    prog += H(0) # number=26
    prog += CZ(1,0) # number=46
    prog += H(0) # number=47
    prog += H(0) # number=27
    prog += H(0) # number=20
    prog += H(0) # number=12
    prog += H(0) # number=28
    prog += CNOT(1,0) # number=37
    prog += H(0) # number=38
    prog += H(0) # number=29
    prog += H(0) # number=13
    prog += H(0) # number=21
    prog += CNOT(1,0) # number=48
    prog += H(0) # number=49
    prog += H(0) # number=22
    prog += H(2) # number=7
    prog += CZ(0,2) # number=50
    prog += H(2) # number=51
    prog += X(2) # number=30
    prog += CNOT(0,2) # number=31
    prog += H(2) # number=9
    prog += H(2) # number=32
    prog += H(2) # number=39
    prog += CZ(3,2) # number=41
    prog += H(2) # number=42
    prog += H(2) # number=40
    prog += H(2) # number=33
    prog += H(2) # number=8
    prog += T(2) # number=14
    prog += T(2) # number=34
    prog += T(2) # number=15
    prog += T(2) # number=23
    prog += H(2) # number=16
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

    writefile = open("startPyquil_statevector_223.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()
