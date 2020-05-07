import random

import FailedAttemptException

class EliminationGenerator:
	def __init__(self, multiplier = 2, offset = -20, a = 30, b = 100, d = 50):
		self.multiplier = multiplier
		self.offset = offset
		self.a = a
		self.b = b
		self.d = d

	def next(self):
		while True:
			try:
				value = self._attempt_generation()
				return value
			except Exception:
				pass

	def debug_generation(self):
		iterations = 10000
		successCnt = 0
		for i in range(0, iterations):
			try:
				self._attempt_generation(debugMode=True)
				successCnt += 1
			except Exception:
				pass
		print(str(successCnt) + " generations were successful out of " + str(iterations) + " attempted")

	def _attempt_generation(self, debugMode = False):
		uOne = random.uniform(self.a, self.b)
		uTwo = random.uniform(0, self.d)
		
		calculatedValue = self._calculate_expression(uOne)
		if uTwo < calculatedValue:
			if debugMode:
				print(str(uTwo) + ": " + str(calculatedValue))
			return calculatedValue
		else:
			raise Exception()

	def _calculate_expression(self, value):
		return (self.multiplier * value + self.offset)
