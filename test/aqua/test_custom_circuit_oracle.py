# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Test Custom Circuit Oracle """

import unittest
from test.aqua.common import QiskitAquaTestCase
from qiskit import BasicAer, QuantumCircuit, QuantumRegister
from qiskit.aqua import QuantumInstance, AquaError
from qiskit.aqua.components.oracles import CustomCircuitOracle
from qiskit.aqua.algorithms import DeutschJozsa
from qiskit.aqua.algorithms import Grover


class TestCustomCircuitOracle(QiskitAquaTestCase):
    """ Test Custom Circuit Oracle """
    def test_using_dj_with_constant_func(self):
        """ using dj with constant func test """
        q_v = QuantumRegister(2, name='v')
        q_o = QuantumRegister(1, name='o')
        circuit = QuantumCircuit(q_v, q_o)
        circuit.x(q_o[0])

        oracle = CustomCircuitOracle(variable_register=q_v, output_register=q_o, circuit=circuit)
        algorithm = DeutschJozsa(oracle)
        result = algorithm.run(
            quantum_instance=QuantumInstance(BasicAer.get_backend('qasm_simulator')))
        self.assertEqual(result['result'], 'constant')

    def test_using_dj_with_balanced_func(self):
        """ using dj with balanced func test """
        q_v = QuantumRegister(2, name='v')
        q_o = QuantumRegister(1, name='o')
        circuit = QuantumCircuit(q_v, q_o)
        circuit.cx(q_v[0], q_o[0])

        oracle = CustomCircuitOracle(variable_register=q_v, output_register=q_o, circuit=circuit)
        algorithm = DeutschJozsa(oracle)
        result = algorithm.run(
            quantum_instance=QuantumInstance(BasicAer.get_backend('qasm_simulator')))
        self.assertEqual(result['result'], 'balanced')


if __name__ == '__main__':
    unittest.main()
