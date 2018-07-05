class Connection:
    def __init__(self, neuron, weight=0):
        self.neuron = neuron
        self.weight = weight

    def connection(self, neuron, weight):
        self.neuron = neuron
        self.weight = weight

    def get_value(self):
        return self.neuron.get_value() * self.weight