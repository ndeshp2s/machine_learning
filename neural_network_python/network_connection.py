#!/usr/bin/python

from weight import Weight 

import math
import random

class NetworkConnection:
    def __init__(self):
        self.weights = []
        self.weight_index = 0
        
    def createConnection(self, inputs, hidden_layers, outputs, nodes):
                
        total_layers = 1 + len(hidden_layers) + 1        
    
        # iterate over all layers
        for i in range(total_layers-1):
            #print ("i = ", i)
            # iterante over all nodes
            for j in range(len(nodes)):
                # find node located in layer i
                if nodes[j].getLayerNumber() == i:
                   # iterate over all nodes 
                   for k in range(len(nodes)):
                       # if k'th node is in the next layer (as that of j'th node) 
                       if nodes[k].getLayerNumber() == i+1:
                           # and if k'th node is not a bias node
                           if nodes[k].getIsBiasUnit() == False:
                               # output of j'th node goes to the input of k'th node                          
                               weight = Weight()
                               weight.setIndex(self.weight_index)
                               weight.setFromNode(nodes[j].getIndex())
                               weight.setToNode(nodes[k].getIndex())
                               weight.setValue(self.generateRand(inputs))
                           
                               self.weight_index = self.weight_index +1                           
                               self.weights.append(weight)
                           
                               print("Weight from " + str(nodes[j].getLabel()) + " to " + str(nodes[k].getLabel()) + " ---> " + str(weight.getValue()))

        return self.weights
                               

    def generateRand(self, inputs):
    # setup rand variable
        range_min = 0
        range_max = 1
        init_epsilon = math.sqrt(6) / (math.sqrt(inputs) + 1)        
        rand = range_min + (range_min + range_max) * random.random()
        rand = rand * (2 * init_epsilon) - init_epsilon
        
        return rand                               
