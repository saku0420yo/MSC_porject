# qubit number=4
# total number=53
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
    prog += H(0) # number=26
    prog += CNOT(2,0) # number=42
    prog += H(0) # number=43
    prog += H(0) # number=27
    prog += CNOT(2,0) # number=16
    prog += Z(2) # number=44
    prog += CNOT(2,0) # number=45
    prog += H(0) # number=17
    prog += H(0) # number=28
    prog += CNOT(2,0) # number=46
    prog += H(0) # number=47
    prog += H(0) # number=29
    prog += H(3)  # number=3
    prog += CNOT(3,0) # number=4
    prog += Z(3) # number=12
    prog += CNOT(3,0) # number=13
    prog += RX(-2.0420352248333655,0) # number=10
    prog += H(0) # number=5
    prog += H(0) # number=14
    prog += H(0) # number=30
    prog += CZ(1,0) # number=48
    prog += H(0) # number=49
    prog += H(0) # number=31
    prog += H(0) # number=15
    prog += H(0) # number=6
    prog += CZ(1,0) # number=50
    prog += H(0) # number=51
    prog += H(0) # number=18
    prog += CZ(1,0) # number=32
    prog += H(0) # number=33
    prog += CNOT(1,0) # number=19
    prog += CNOT(1,3) # number=11
    prog += H(3) # number=20
    prog += CZ(1,3) # number=34
    prog += H(3) # number=35
    prog += CNOT(1,3) # number=21
    prog += CNOT(0,2) # number=7
    prog += CNOT(0,2) # number=22
    prog += X(2) # number=36
    prog += CNOT(0,2) # number=37
    prog += H(2) # number=23
    prog += H(2) # number=38
    prog += CNOT(0,2) # number=52
    prog += H(2) # number=53
    prog += H(2) # number=39
    prog += H(2) # number=9
    prog += H(2) # number=24
    prog += CNOT(3,2) # number=40
    prog += H(2) # number=41
    prog += H(2) # number=25
    prog += H(2) # number=8
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
    writefile = open("startPyquil229.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

