#!/usr/bin/python
from network_calculation import NetworkCalculation

class NetworkLearning:
    
    def backPropogation(self, nodes, weights, , learning_rate, features):

    	number_of_features = len(features[1]) - 1

    	for i in range(len(features)):
    		# apply forward propogation first
    		nodes = NetworkCalculation.forwardPropogation(nodes, weights, instances[i])

    		predicted_output = nodes[len(nodes) - 1].getNetOutputValue()
    		actual_output = instances[i][number_of_features]





    	return nodes, weights