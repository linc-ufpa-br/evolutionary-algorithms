from psoadriana.particle import Particle
import numpy as np
class Swarm:

    def __init__(self, inertia_ini, inertia_final, ci, si, max_velocity):
        self._particles = []
        self._global_best_position = None # melhor posicao global
        self._global_best_value = np.inf  # melhor valor global
        self._inertia_ini = inertia_ini  # valor da inercia inicial
        self._inertia_final = inertia_final  # valor da inercia final
        self._ci = ci  # valor da constante de informação cognitiva
        self._si = si  # valor da constante de informação social
        self._max_velocity = max_velocity # maior valor de velocidade

    @property
    def particles(self):
        return self._particles

    def inertia(self, iteration_t, iteration_final):
        """ retorna o valor da inércia a ser usado, conforme a iteração atual e iteração máxima do algoritmo"""
        return self._inertia_final - (self._inertia_final - self._inertia_ini) * (iteration_t / iteration_final)

    def init_particles(self, particles_length, low, high, size, function_avaliation):
        """ inicia as particulas da população """
        particles = []
        for i in range(particles_length):  # inicia a população de particulas
            particle = Particle(low, high, size, function_avaliation)
            particles.append(particle)
        self._particles = particles
        self.check_best_global_result()

    def updateSwarm(self, iteration_t, iteration_final):
        # print(self._global_best_value)
        # print(self._global_best_position)
        """ atualiza as particulas da população """
        inertia = self.inertia(iteration_t, iteration_final)
        for p in self._particles:  # atualiza as particulas
            p.update_velocity(inertia, self._ci, self._si, self._global_best_position, self._max_velocity)
            p.update_position()
            p.evaluate()
        self.check_best_global_result()

    def check_best_global_result(self):
        self._particles = sorted(self._particles, key=lambda x: x.best_value)  # ordena a população em ordem decrescente pelo melhor valor
        if self._particles[0].best_value < self._global_best_value: # verifica se um melhor global foi encontrado e atualiza
            self._global_best_position = self._particles[0].best_position
            self._global_best_value = self._particles[0].best_value

