# qubit number=4
# total number=82
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program('PRAGMA INITIAL_REWIRING "GREEDY"') # circuit begin


    prog += H(1)  # number=1
    prog += H(0) # number=2
    prog += T(0) # number=21
    prog += T(0) # number=71
    prog += T(0) # number=22
    prog += T(0) # number=40
    prog += H(0) # number=23
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += RX(-2.0420352248333655,0) # number=5
    prog += H(0) # number=6
    prog += H(0) # number=14
    prog += H(0) # number=26
    prog += CZ(1,0) # number=45
    prog += H(0) # number=46
    prog += H(0) # number=27
    prog += H(0) # number=15
    prog += H(0) # number=7
    prog += H(0) # number=47
    prog += H(0) # number=60
    prog += CZ(1,0) # number=72
    prog += H(0) # number=73
    prog += H(0) # number=61
    prog += H(0) # number=48
    prog += H(0) # number=32
    prog += CZ(1,0) # number=62
    prog += H(0) # number=63
    prog += H(0) # number=33
    prog += H(0) # number=41
    prog += H(0) # number=49
    prog += CZ(1,0) # number=64
    prog += H(0) # number=65
    prog += H(0) # number=50
    prog += H(0) # number=42
    prog += H(2) # number=8
    prog += T(2) # number=16
    prog += T(2) # number=51
    prog += T(2) # number=17
    prog += T(2) # number=52
    prog += H(2) # number=18
    prog += H(1) # number=12
    prog += CZ(2,1) # number=24
    prog += H(1) # number=25
    prog += H(2) # number=9
    prog += H(2) # number=28
    prog += H(2) # number=34
    prog += CZ(3,2) # number=43
    prog += H(2) # number=44
    prog += H(2) # number=35
    prog += H(2) # number=29
    prog += T(2) # number=10
    prog += T(2) # number=66
    prog += S(2) # number=53
    prog += H(3) # number=13
    prog += H(3) # number=36
    prog += CNOT(0,3) # number=54
    prog += H(3) # number=55
    prog += H(3) # number=37
    prog += H(3) # number=19
    prog += CZ(0,3) # number=74
    prog += H(3) # number=75
    prog += CNOT(0,3) # number=38
    prog += CNOT(0,3) # number=56
    prog += H(3) # number=67
    prog += S(3) # number=76
    prog += S(3) # number=77
    prog += H(3) # number=78
    prog += H(3) # number=68
    prog += CZ(0,3) # number=79
    prog += H(3) # number=80
    prog += CNOT(0,3) # number=57
    prog += H(3) # number=39
    prog += H(3) # number=58
    prog += CNOT(0,3) # number=81
    prog += H(3) # number=82
    prog += H(3) # number=59
    prog += H(3) # number=20
    prog += CZ(0,3) # number=30
    prog += H(3) # number=31
    prog += H(2) # number=11
    prog += CZ(1,2) # number=69
    prog += H(2) # number=70
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
    qvm = get_qc('4q-qvm')

    results = qvm.run_and_measure(prog,1024)
    bitstrings = np.vstack([results[i] for i in qvm.qubits()]).T
    bitstrings = [''.join(map(str, l)) for l in bitstrings]
    writefile = open("startPyquil_pragma_225.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

