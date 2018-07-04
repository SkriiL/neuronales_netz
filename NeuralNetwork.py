from InputNeuron import InputNeuron
from WorkingNeuron import WorkingNeuron


class NeuralNetwork:
    def __init__(self):
        self.input_neurons = []
        self.output_neurons = []

    def create_new_output(self):
        wn_neuron = WorkingNeuron()
        self.output_neurons.append(wn_neuron)
        return wn_neuron

    def create_new_input(self):
        in_neuron = InputNeuron()
        self.input_neurons.append(in_neuron)
        return in_neuron