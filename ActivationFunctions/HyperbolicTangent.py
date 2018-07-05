import math


class HyperbolicTangent:
    def activation(self, input):
        epx = float(math.exp(input))
        enx = float(math.exp(-input))

        return (epx - enx) / (epx + enx)