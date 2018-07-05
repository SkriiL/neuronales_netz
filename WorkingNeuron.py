from ActivationFunctions import Boolean, Identity, Sigmoid, HyperbolicTangent

class WorkingNeuron():
    def __init__(self):
        self.connections = []
        self.activation_fn = Identity.Identity()

    def get_value(self):
        sum = 0
        for c in self.connections:
            sum += c.get_value()
        return self.activation_fn.activation(sum)

    def add_connection(self, c):
        self.connections.append(c)