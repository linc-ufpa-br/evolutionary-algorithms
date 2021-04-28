import numpy as np


class Particle:
    def __init__(self, low, high, size, function_avaliation):
        self._low = low
        self._high = high
        self._function_avaliation = function_avaliation
        self._position = np.random.randint(low,high+1, size)  # posição atual da particula
        self._velocity = np.zeros(size) # velocidade atual da particula
        self._value = self._function_avaliation.evaluate(self._position)  # valor atual da particula
        self._best_position = self._position  # melhor posição da particula
        self._best_value = self._value  # melhor valor da particula
        self._decode = []

    @property
    def best_value(self):
        return self._best_value

    @property
    def best_position(self):
        return self._best_position

    def __str__(self):
        #return "best_value {} value {} {}".format(self._best_value, self._value, super.__str__(self))
        return "best_value {} best_position {} velocity {}, value {} position {} decode {} {}".format(self._best_value, self._best_position.astype(int), self._velocity, self._value, self._position, self._decode, super.__str__(self))

    def evaluate(self):
        # print('init value personal ' + str(self._value))
        self._value = self._function_avaliation.evaluate(self._position)
        decode = self._function_avaliation.decode(self._position)
        # print('final value personal ' + str(self._value))
        """ se a posição atual for melhor que a melhor posição da particula, então deve receber a nova posição """
        if self._value < self._best_value:
            self._best_value = self._value
            self._best_position = self._position
            self._decode = decode
        # print(self._best_value)

    def update_position(self):
        # print('posicao inicial ' + str(self._position))
        position_not_verified = self._position + self._velocity
        self._position = np.clip(position_not_verified, self._low, self._high)
        # print('posicao final ' + str(self._position))

    def update_velocity(self, inertia_weight, cognitive_weight, social_weight, best_global_position, max_velocity):
        # print('velocidade inicial ' + str(self._velocity))
        length_array = len(self._position)
        r1 = np.random.random(length_array)
        r2 = np.random.random(length_array)
        cognitive_component = cognitive_weight * r1 * (self._best_position - self._position)
        social_component = social_weight * r2 * (best_global_position - self._position)
        uncontrolled_velocity = self._velocity * inertia_weight + cognitive_component + social_component
        self._velocity = np.clip(uncontrolled_velocity, -max_velocity, max_velocity)
        # print('velocidade final ' + str(self._velocity))







