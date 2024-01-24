# JOSE ANTONIO DIAZ ARANDA
import numpy as np
class Neuron:
    def __init__(self, weights, bias, func):
        self.weights = np.array(weights)
        self.bias = bias
        self.activation_function = {
            'relu':self._relu,
            'sigmoid':self._sigmoid,
            'tanh':self._tanh
              }
        self.func = func

    @staticmethod
    def _relu(y):
        return max(0, y)

    @staticmethod
    def _sigmoid(y):
        return 1 / (1 + np.exp(-y))

    @staticmethod
    def _tanh(y):
        return np.tanh(y)

    def run(self, input_data):
        y = np.dot(input_data, self.weights) + self.bias
        output = self.activation_function[self.func](y)
        return output

    def change_weights(self, new_weights):
        self.weights = np.array(new_weights)

    def change_bias(self, new_bias):
        self.bias = new_bias