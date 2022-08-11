# qubit number=4
# total number=71
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=1
    prog += RX(-0.24818581963359365,2) # number=10
    prog += T(2) # number=2
    prog += T(2) # number=56
    prog += T(2) # number=30
    prog += T(2) # number=44
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += H(0) # number=5
    prog += H(0) # number=12
    prog += H(0) # number=31
    prog += CZ(1,0) # number=65
    prog += H(0) # number=66
    prog += H(0) # number=32
    prog += H(0) # number=13
    prog += H(0) # number=6
    prog += H(0) # number=33
    prog += H(0) # number=45
    prog += CZ(1,0) # number=67
    prog += H(0) # number=68
    prog += H(0) # number=46
    prog += H(0) # number=34
    prog += H(0) # number=14
    prog += H(0) # number=18
    prog += H(0) # number=26
    prog += CZ(1,0) # number=35
    prog += H(0) # number=36
    prog += H(0) # number=27
    prog += H(0) # number=19
    prog += H(0) # number=15
    prog += H(0) # number=20
    prog += CNOT(1,0) # number=47
    prog += H(0) # number=48
    prog += H(0) # number=21
    prog += H(2) # number=7
    prog += H(2) # number=22
    prog += H(2) # number=49
    prog += CZ(0,2) # number=57
    prog += H(2) # number=58
    prog += H(2) # number=50
    prog += H(2) # number=23
    prog += H(2) # number=16
    prog += CZ(0,2) # number=51
    prog += H(2) # number=52
    prog += H(2) # number=37
    prog += S(2) # number=69
    prog += S(2) # number=70
    prog += H(2) # number=71
    prog += H(2) # number=38
    prog += CZ(0,2) # number=59
    prog += H(2) # number=60
    prog += H(2) # number=17
    prog += H(2) # number=24
    prog += H(2) # number=53
    prog += CZ(0,2) # number=61
    prog += H(2) # number=62
    prog += H(2) # number=54
    prog += H(2) # number=25
    prog += H(2) # number=9
    prog += H(2) # number=39
    prog += CNOT(3,2) # number=63
    prog += H(2) # number=64
    prog += H(2) # number=40
    prog += H(1) # number=11
    prog += CZ(2,1) # number=28
    prog += H(1) # number=29
    prog += H(2) # number=8
    prog += T(2) # number=41
    prog += T(2) # number=55
    prog += S(2) # number=42
    prog += H(2) # number=43
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

    writefile = open("startPyquil_statevector_230.csv","w")
    print(state.get_outcome_probs(),file=writefile)
    writefile.close()

