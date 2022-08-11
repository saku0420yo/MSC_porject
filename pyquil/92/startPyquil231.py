# qubit number=4
# total number=60
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
    prog += H(0) # number=10
    prog += CZ(3,0) # number=38
    prog += H(0) # number=39
    prog += H(0) # number=15
    prog += CZ(3,0) # number=40
    prog += H(0) # number=41
    prog += CNOT(3,0) # number=25
    prog += Z(3) # number=54
    prog += CNOT(3,0) # number=55
    prog += H(0) # number=26
    prog += CZ(3,0) # number=42
    prog += H(0) # number=43
    prog += CNOT(3,0) # number=16
    prog += H(0) # number=5
    prog += CZ(1,0) # number=29
    prog += H(0) # number=30
    prog += H(3) # number=6
    prog += CZ(2,3) # number=56
    prog += H(3) # number=57
    prog += H(3) # number=31
    prog += CZ(2,3) # number=44
    prog += H(3) # number=45
    prog += H(3) # number=32
    prog += CZ(2,3) # number=46
    prog += H(3) # number=47
    prog += CNOT(3,1) # number=12
    prog += CNOT(3,1) # number=48
    prog += H(1) # number=49
    prog += CZ(3,1) # number=58
    prog += H(1) # number=59
    prog += H(2) # number=7
    prog += T(2) # number=17
    prog += T(2) # number=33
    prog += T(2) # number=18
    prog += T(2) # number=27
    prog += H(2) # number=19
    prog += H(2) # number=9
    prog += H(2) # number=34
    prog += CNOT(3,2) # number=50
    prog += H(2) # number=51
    prog += H(2) # number=35
    prog += CNOT(3,0) # number=11
    prog += CNOT(3,0) # number=36
    prog += Z(3) # number=52
    prog += CNOT(3,0) # number=53
    prog += CNOT(3,0) # number=37
    prog += H(2) # number=8
    prog += T(2) # number=20
    prog += T(2) # number=28
    prog += T(2) # number=21
    prog += T(2) # number=60
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
    qvm = get_qc('4q-qvm')

    results = qvm.run_and_measure(prog,1024)
    bitstrings = np.vstack([results[i] for i in qvm.qubits()]).T
    bitstrings = [''.join(map(str, l)) for l in bitstrings]
    writefile = open("startPyquil231.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

