#!/usr/bin/python

class Node:
	index = 0
	label = 0
	is_bias_unit = False

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