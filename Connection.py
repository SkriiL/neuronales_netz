from Neuron import Neuron


class Connection:
    def __init__(self):
        self.neuron = Neuron
        self.weight = 0

    def connection(self, neuron, weight):
        self.neuron = neuron
        self.weight = weight

    def get_value(self):
        return self.neuron.get_value() * self.weight
