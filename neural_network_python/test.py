#!/usr/bin/python
from network_structure import NetworkStructure
from network_connection import NetworkConnection
        
if __name__ == "__main__":
    # Create a data set (for OR gate)
    instances = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

    # Find the number of features
    number_of_features = len(instances[0]) - 1 
    
    inputs = number_of_features
    hidden_layers = [3, 3]
    outputs = 1
    
    nn_network = NetworkStructure()
    nn_weights = NetworkConnection()

    nodes = nn_network.createNetwork(inputs, hidden_layers, outputs)	
    
    weights = nn_weights.createConnection(inputs, hidden_layers, outputs, nodes)

               

