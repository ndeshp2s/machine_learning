#!/usr/bin/python

from node import Node

class NetworkStructure:

    def __init__(self, inputs, hidden_layers, outputs):
        self.inputs = inputs
        self.hidden_layers = hidden_layers
        self.outputs = outputs
        self.nodes = []
        self.node_index = 0
        
        print ("Creating the Network")
        
        #-----------------------#
        #----- input layer -----#
        
        # bias unit
        self.createNode(True)
        print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
        
        #inputs
        for i in range(self.inputs):
            self.createNode(False, "x"+str(i+1)) 
            print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            
        print("\n")    
                
        #-------------------------#
        #----- hidden layers -----#
        
        #nodes
        for i in range(len(self.hidden_layers)):
            
            self.createNode(True)
            print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            
            for j in range(self.hidden_layers[i]): 
                self.createNode(False, "h"+str(i+1)+str(j+1))  
                print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            print("\n")
        #print("\n")    
        
        #-------------------------#
        #----- output layer -----#
        
        #outputss
        for o in range(self.outputs):
            self.createNode(False, "o"+str(o+1)) 
            print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            
        print("\n") 
                        
        
               

    def createNode(self, bias, label = None):	
        node = Node()
        
        if (bias == True):
            node.setLabel("+1")
            node.setIsBiasUnit(True)
            node.setIndex(self.node_index)
        else:
            node.setLabel(label)
            node.setIsBiasUnit(False)
            node.setIndex(self.node_index)

        self.nodes.append(node)
        self.node_index = self.node_index + 1
	
    