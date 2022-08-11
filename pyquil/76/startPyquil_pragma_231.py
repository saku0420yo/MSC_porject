# qubit number=4
# total number=41
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program('PRAGMA INITIAL_REWIRING "GREEDY"') # circuit begin


    prog += H(1)  # number=1
    prog += RX(-0.38013271108436497,2) # number=11
    prog += H(1) # number=14
    prog += CZ(2,1) # number=26
    prog += H(1) # number=27
    prog += CNOT(2,1) # number=15
    prog += H(1) # number=16
    prog += CZ(2,1) # number=36
    prog += H(1) # number=37
    prog += RX(-0.24818581963359365,2) # number=10
    prog += RX(-0.38013271108436497,2) # number=11
    prog += H(1) # number=14
    prog += CZ(2,1) # number=28
    prog += H(1) # number=29
    prog += H(1) # number=17
    prog += CZ(2,1) # number=24
    prog += H(1) # number=25
    prog += H(1) # number=18
    prog += CZ(2,1) # number=30
    prog += H(1) # number=31
    prog += Z(2)  # number=2
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += H(0) # number=5
    prog += H(0) # number=19
    prog += CNOT(1,0) # number=32
    prog += H(0) # number=33
    prog += H(0) # number=20
    prog += SWAP(1,0) # number=6
    prog += RX(1.168672467135403,1) # number=12
    prog += H(2) # number=7
    prog += CZ(0,2) # number=38
    prog += H(2) # number=39
    prog += X(2) # number=34
    prog += CNOT(0,2) # number=35
    prog += CNOT(1,2) # number=13
    prog += H(2) # number=9
    prog += H(2) # number=21
    prog += CNOT(3,2) # number=40
    prog += H(2) # number=41
    prog += H(2) # number=22
    prog += S(2) # number=8
    prog += S(2) # number=23
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
    writefile = open("startPyquil_pragma_231.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

