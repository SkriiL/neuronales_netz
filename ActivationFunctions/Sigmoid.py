import math

class Sigmoid:
    def activation(self, input):
        return float(1 / (1 + math.exp(-input)))
