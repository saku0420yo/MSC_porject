# qubit number=4
# total number=59
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
    prog += T(2) # number=33
    prog += T(2) # number=12
    prog += T(2) # number=34
    prog += CNOT(3,0) # number=3
    prog += CNOT(3,0) # number=22
    prog += CNOT(3,0) # number=35
    prog += Z(3) # number=49
    prog += CNOT(3,0) # number=50
    prog += H(0) # number=36
    prog += CZ(3,0) # number=51
    prog += H(0) # number=52
    prog += H(0) # number=23
    prog += CZ(3,0) # number=53
    prog += H(0) # number=54
    prog += Y(3) # number=4
    prog += H(0) # number=5
    prog += H(0) # number=13
    prog += CNOT(1,0) # number=44
    prog += H(0) # number=45
    prog += H(0) # number=14
    prog += CNOT(1,0) # number=6
    prog += H(0) # number=15
    prog += H(0) # number=24
    prog += CNOT(1,0) # number=37
    prog += H(0) # number=38
    prog += H(0) # number=25
    prog += H(0) # number=16
    prog += H(0) # number=26
    prog += CNOT(1,0) # number=39
    prog += H(0) # number=40
    prog += H(0) # number=27
    prog += H(2) # number=7
    prog += T(2) # number=17
    prog += T(2) # number=41
    prog += T(2) # number=18
    prog += T(2) # number=46
    prog += H(2) # number=19
    prog += H(2) # number=9
    prog += H(2) # number=28
    prog += CNOT(3,2) # number=47
    prog += H(2) # number=48
    prog += H(2) # number=29
    prog += H(2) # number=8
    prog += H(2) # number=20
    prog += H(2) # number=42
    prog += CZ(0,2) # number=55
    prog += H(2) # number=56
    prog += H(2) # number=43
    prog += H(2) # number=21
    prog += H(2) # number=10
    prog += S(2) # number=30
    prog += T(2) # number=31
    prog += T(2) # number=57
    prog += H(2) # number=32
    prog += H(2) # number=11
    prog += CZ(0,2) # number=58
    prog += H(2) # number=59
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
    writefile = open("startPyquil228.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

