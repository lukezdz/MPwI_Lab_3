import random

class InvertedDistributionGenerator:
	def __init__(self, intervals = [0.2, 0.4, 0.3, 0.1]):
		self.intervals = intervals
		self.maxValue = 0
		for val in intervals:
			self.maxValue += val

	
	def next(self):
		value = random.uniform(0, self.maxValue)
		currentSum = 0
		
		if value == 0:
			return 0

		for i in range(0, len(self.intervals)):
			if value >= currentSum and value < currentSum + self.intervals[i]:
				return i + 1
			else:
				currentSum += self.intervals[i]
