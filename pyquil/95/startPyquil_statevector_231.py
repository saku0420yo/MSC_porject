# qubit number=4
# total number=62
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += H(2) # number=2
    prog += H(2) # number=34
    prog += CNOT(0,2) # number=45
    prog += H(2) # number=46
    prog += H(2) # number=35
    prog += H(2) # number=10
    prog += S(2) # number=52
    prog += S(2) # number=53
    prog += H(2) # number=54
    prog += CNOT(0,2) # number=11
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += H(3) # number=5
    prog += H(3) # number=19
    prog += H(3) # number=27
    prog += CZ(0,3) # number=55
    prog += H(3) # number=56
    prog += H(3) # number=28
    prog += H(3) # number=20
    prog += H(3) # number=12
    prog += T(3) # number=29
    prog += T(3) # number=36
    prog += T(3) # number=30
    prog += T(3) # number=47
    prog += H(3) # number=31
    prog += H(3) # number=13
    prog += H(3) # number=21
    prog += H(3) # number=37
    prog += CZ(0,3) # number=48
    prog += H(3) # number=49
    prog += H(3) # number=38
    prog += H(3) # number=22
    prog += H(0) # number=6
    prog += H(0) # number=39
    prog += H(0) # number=50
    prog += CZ(1,0) # number=57
    prog += H(0) # number=58
    prog += H(0) # number=51
    prog += H(0) # number=40
    prog += H(0) # number=14
    prog += CZ(1,0) # number=59
    prog += H(0) # number=60
    prog += H(0) # number=15
    prog += H(0) # number=23
    prog += H(0) # number=32
    prog += CZ(1,0) # number=61
    prog += H(0) # number=62
    prog += H(0) # number=33
    prog += H(0) # number=24
    prog += H(2) # number=7
    prog += T(2) # number=16
    prog += T(2) # number=25
    prog += T(2) # number=17
    prog += T(2) # number=26
    prog += H(2) # number=18
    prog += H(2) # number=8
    prog += CZ(3,2) # number=41
    prog += H(2) # number=42
    prog += CNOT(0,2) # number=9
    prog += X(2) # number=43
    prog += CNOT(0,2) # number=44
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

    writefile = open("startPyquil_statevector_231.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()

