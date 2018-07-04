from Neuron import Neuron


class InputNeuron(Neuron):
    def __init__(self):
        super().__init__(self, Neuron)
        self.value = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value