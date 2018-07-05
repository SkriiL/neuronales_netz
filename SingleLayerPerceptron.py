from NeuralNetwork import NeuralNetwork

nn = NeuralNetwork()

i1 = nn.create_new_input()
i2 = nn.create_new_input()
i3 = nn.create_new_input()

o1 = nn.create_new_output()

#nn.create_full_mesh([])

right = False
counter = 0
weights = []

i1.set_value(1)
i2.set_value(2)
i3.set_value(3)

nn.train(0)

value = o1.get_value()

while not right:
    value = o1.get_value()
    print(counter, ": ", value)
    right, weights = nn.train(counter=counter, weights=weights, value=value, rate=0.07)
    counter += 1
