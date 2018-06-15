#!/usr/bin/python

class Node:
	index = 0
	label = 0
	is_bias_unit = False
	layer_number = 0
	net_input_value = 0
	net_output_value = 0

	def setIndex(self, index):
		self.index = index

	def getIndex(self):
		return self.index

	def setLabel(self, label):
		self.label = label

	def getLabel(self):
		return self.label

	def setIsBiasUnit(self, is_bias_unit):
		self.is_bias_unit = is_bias_unit

	def getIsBiasUnit(self):
		return self.is_bias_unit

	def setLayerNumber(self, layer):
		self.layer_number = layer

	def getLayerNumber(self):
		return self.layer_number
  
	def setNetInputValue(self, net_input_value):
		self.net_input_value = net_input_value

	def getNetInputValue(self):
		return self.net_input_value  

	def setNetOutputValue(self, net_output_value):
		self.net_output_value = net_output_value

	def getNetOutputValue(self):
		return self.net_output_value	
  