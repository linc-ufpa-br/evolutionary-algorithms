import numpy as np
from .function_fitness import FunctionFitness


class SurgeriesFunction(FunctionFitness):

    def __init__(self):
        self._rooms = 7
        self._surgeries = [[4, 47, 13], [3, 10, 29], [2, 33, 33], [1, 25, 79]]

    def calc_fitness(self, chromossome):
        index = 0
        time_rooms = np.zeros(self._rooms)
        for surgery in self._surgeries:  # para toda cirurgia
            for i in range(surgery[2]):  # para toda quantidade de uma cirurgia
                room = chromossome[index]
                time_rooms[room] += surgery[1]
                index += 1
        return 1.0/np.amax(time_rooms), time_rooms