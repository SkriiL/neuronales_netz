from Neuron import Neuron


class WorkingNeuron(Neuron):
    def __init__(self):
        super().__init__(self, Neuron)
        self.connections = []

    def get_value(self):
        sum = 0
        for c in self.connections:
            sum += c.get_value()
        return sum


