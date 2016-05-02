__author__ = 'Ahmed Hani Ibrahim'

from input_processing import InputProcessing
from particle_package import particle_algorithm
from statistics import normalize
from util import matrix_operations
import numpy as np

matrix = [[5, 2, 4, 4, 3], [3, 1, 2, 4, 1], [2, -1, 3, 1, 4], [2, 5, 4, 3, 5], [4, 4, 5, 4, -1]]

input_processing = InputProcessing(matrix)

input_processing.set_u_sizes(5, 2)
input_processing.set_v_sizes(2, 5)

u = input_processing.get_u()
v = input_processing.get_v()

particle_swarm = particle_algorithm.ParticleAlgorithm(200, len(matrix) * len(matrix[0]), u, v, matrix)

error = particle_swarm.optimize(0.1, 2000)
u = particle_swarm.get_matrix_u()
v = particle_swarm.get_matrix_v()

print(u)
print(v)
print(error)

result = matrix_operations.matrix_multiplication(u, v)
result = normalize.matrix_normalization(result, 5.0, 1.0)

print(np.array(result))


