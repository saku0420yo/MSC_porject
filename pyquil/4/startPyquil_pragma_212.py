# qubit number=4
# total number=19
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program('PRAGMA INITIAL_REWIRING "GREEDY"') # circuit begin


    prog += H(1)  # number=1
    prog += RX(-0.24818581963359365,2) # number=10
    prog += Z(2)  # number=2
    prog += H(3)  # number=3
    prog += Y(3) # number=4
    prog += CNOT(1,0) # number=5
    prog += CNOT(1,0) # number=6
    prog += CNOT(1,0) # number=15
    prog += CNOT(1,0) # number=16
    prog += H(2) # number=7
    prog += S(2) # number=11
    prog += S(2) # number=12
    prog += H(2) # number=13
    prog += H(2) # number=9
    prog += CZ(3,2) # number=17
    prog += H(2) # number=18
    prog += T(2) # number=8
    prog += T(2) # number=19
    prog += S(2) # number=14
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
    writefile = open("startPyquil_pragma_212.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()
