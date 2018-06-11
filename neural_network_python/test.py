#!/usr/bin/python
from network_structure import NetworkStructure
        
if __name__ == "__main__":
    # Create a data set (for OR gate)
    instances = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

    # Find the number of features
    number_of_features = len(instances[0]) - 1 
    
    inputs = number_of_features
    hidden_layers = [2, 3]
    outputs = 1

    network = NetworkStructure(inputs, hidden_layers, outputs)	
