from InputNeuron import InputNeuron
from WorkingNeuron import WorkingNeuron
from Connection import Connection

import random


class NeuralNetwork:
    def __init__(self):
        self.input_neurons = []
        self.output_neurons = []
        self.hidden_neurons = []
        self.counter = 0

    def create_new_output(self):
        w_neuron = WorkingNeuron()
        self.output_neurons.append(w_neuron)
        return w_neuron

    def create_new_input(self):
        i_neuron = InputNeuron()
        self.input_neurons.append(i_neuron)
        return i_neuron

    def create_hidden_neurons(self, amount):
        for i in range(0, amount):
            self.hidden_neurons.append(WorkingNeuron())

    #def create_full_mesh(self):
    #    if len(self.hidden_neurons) == 0:
    #        for w_neuron in self.output_neurons:
    #            for i_neuron in self.input_neurons:
    #                w_neuron.add_connection(Connection(i_neuron, 0))
    #    else:
    #        for out_neuron in self.output_neurons:
    #            for hid_neuron in self.hidden_neurons:
    #                out_neuron.add_connection(Connection(hid_neuron, 0))
    #        for hid_neuron in self.hidden_neurons:
    #            for in_neuron in self.hidden_neurons:
    #                hid_neuron.add_connection(Connection(in_neuron, 0))

    def create_full_mesh(self, weights):
        if len(self.hidden_neurons) == 0:
            if len(weights) != len(self.input_neurons) * len(self.output_neurons):
                raise Exception

            index = 0

            for w_neuron in self.output_neurons:
                for i_neuron in self.input_neurons:
                    w_neuron.add_connection(Connection(i_neuron, weights[index]))
                    index += 1
        else:
            if len(weights) != len(self.input_neurons) * len(self.hidden_neurons) + len(self.hidden_neurons) * len(self.output_neurons):
                raise Exception

            index = 0

            for hid_neuron in self.hidden_neurons:
                for in_neuron in self.input_neurons:
                    hid_neuron.add_connection(Connection(in_neuron, weights[index]))
                    index += 1

            for out_neuron in self.output_neurons:
                for hid_neuron in self.hidden_neurons:
                    out_neuron.add_connection(Connection(hid_neuron, weights[index]))
                    index += 1

    def train(self, counter=0, weights=[], value=0, rate=0.5):
        weights = weights
        goal = 2
        if value > goal + 0.00001 or value < goal - 0.00001:
            if counter == 0:
                floats = []
                float = 0.0
                while float < 1.0:
                    floats.append(float)
                    float += 0.01
                for out_neuron in self.output_neurons:
                    out_neuron.connections = []
                    for in_neuron in self.input_neurons:
                        weight = random.choice(floats)
                        weights.append(weight)
                        out_neuron.add_connection(Connection(in_neuron, weight))
            else:
                for out_neuron in self.output_neurons:
                    out_neuron.connections = []
                    for i in range(0, len(self.input_neurons)):
                        weight_change = rate * (goal - value) * self.input_neurons[i].get_value()
                        weight = weights[i] + weight_change
                        weights[i] = weight
                        out_neuron.add_connection(Connection(self.input_neurons[i], weight))
            return False, weights
        elif goal + 0.00001 > value > goal - 0.00001:
            return True, weights




