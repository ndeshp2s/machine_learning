#!/usr/bin/python

from node import Node

class NetworkStructure:

    def __init__(self):
        self.nodes = []
        self.node_index = 0
        
    def createNetwork(self, inputs, hidden_layers, outputs):   
        
        self.nodes = []
        self.node_index = 0
        
        print ("Creating the Network Structure")
        
        #---------------------------------#
        #---------- input layer ----------#
        
        # bias unit
        self.createNode(True, 0)
        print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
        
        #inputs
        for i in range(inputs):
            self.createNode(False, 0, "x"+ str(i+1)) 
            print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            
        print("\n")    
                
        #-----------------------------------#
        #---------- hidden layers ----------#
        
        #nodes
        for i in range(len(hidden_layers)):
            
            self.createNode(True, i+1)
            
            print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            
            for j in range(hidden_layers[i]): 
                self.createNode(False, i+1, "h"+str(i+1)+str(j+1))  
                print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            print("\n")    
        
        #-----------------------------------#
        #---------- output layer -----------#
        
        #outputss
        for o in range(outputs):
            self.createNode(False, len(hidden_layers) + 1, "o"+str(o+1)) 
            print(self.nodes[self.node_index-1].getLabel(), "\t", end='')
            
        print("\n") 
        
        return self.nodes
                        
        
               

    def createNode(self, bias, layer_number, label = None):	
        node = Node()
        
        if (bias == True):
            node.setLabel("+1")
            node.setIsBiasUnit(True)
           
        else:
            node.setLabel(label)
            node.setIsBiasUnit(False)
            
        node.setIndex(self.node_index)
        node.setLayerNumber(layer_number)

        self.nodes.append(node)
        self.node_index = self.node_index + 1
	
    