from psoadriana.swarm import Swarm
import copy

class PSO:
    def __init__(self, max_interation=1, max_execution=1):
        self._max_interation = max_interation
        self._max_execution = max_execution
        self._result = []

    @property
    def result(self):
        return self._result

    def exec_algorithm(self, particles_length, inertial_ini, inertial_final, ci, si, function_evaluation, max_velocity, low, high, size):
        for e in range(self._max_execution):
            swarm = Swarm(inertial_ini, inertial_final, ci, si, max_velocity)
            swarm.init_particles(particles_length, low, high, size, function_evaluation)
            execution_list = []
            execution_list.append(copy.deepcopy(swarm.particles))
            for i in range(self._max_interation):
                # print('iteracao ex' + str(i))
                swarm.updateSwarm(i, self._max_interation)
                execution_list.append(copy.deepcopy(swarm.particles))
            self._result.append(execution_list)
