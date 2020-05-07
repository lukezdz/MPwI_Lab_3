from InvertedDistributionGenerator import InvertedDistributionGenerator
from EliminationGenerator import EliminationGenerator

def menu():
	print("")
	print("What would you like to do?")
	print("1. Generate one value with Inverted Distribution Generator")
	print("2. Generate multiple values with Inverted Distribution Generator")
	print("3. Generate one value with Elimination Generator")
	print("4. Generate multiple values with Elimination Generator")
	print("5. Generate 10000 values with Elimination Generator and see how many succeeded")
	print("6. Recreate Inverted Distribution Generator with different values")
	print("7. Recreate Elimination Generator with different values")
	print("8. Quit")

def handleRecreationInvDistGenerator():
	print("Disclaimer: Max value generated by the Inverted Distribution Generator is going to be the amount of intervals")
	print("By default there are 4 intervals: [0.2, 0.4, 0.3, 0.1]")
	print("Set number of intervals")
	intervalsLen = int(input("> "))
	print("Set intervals")
	intervals = []
	for i in range(0, intervalsLen):
		value = float(input(str(i+1) + ": "))
		intervals.append(value)
	return InvertedDistributionGenerator(intervals)

def handleRecreationEliminationGenerator():
	print("Disclaimer: The lower multiplier and offset are the lower is the chance of successful generation")
	print("Set equation's multiplier (a in linear equations), default: 2")
	multiplier = int(input("> "))
	print("Set equation's offset (b in linear equations), default: -20")
	offset = int(input("> "))
	print("Set a (for ranges of rand numbers), default: 30")
	a = int(input("> "))
	print("Set b (for ranges of rand numbers), default: 100")
	b = int(input("> "))
	print("Set d (for ranges of rand numbers), default: 50")
	d = int(input("> "))
	return EliminationGenerator(multiplier, offset, a, b, d)

def howMany():
	print("How many values would you like to generate?")
	return int(input("> "))

if __name__ == "__main__":
	invDistGenerator = InvertedDistributionGenerator()
	eliminationGenerator = EliminationGenerator()

	print("Would you like to create Inverted Distribution Generator with custom values? (y/n)")
	choice = input("> ")
	if choice == "y":
		invDistGenerator = handleRecreationInvDistGenerator()

	print("Would you like to create Elimination Generator with custom values? (y/n)")
	choice = input("> ")
	if choice == "y":
		eliminationGenerator = handleRecreationEliminationGenerator()

	while True:
		menu()
		choice = input("> ")

		if choice == "1":
			print(invDistGenerator.next())
		elif choice == "2":
			iterations = howMany()
			for i in range(0, iterations):
				print(invDistGenerator.next())
		elif choice == "3":
			print(eliminationGenerator.next())
		elif choice == "4":
			iterations = howMany()
			for i in range(0, iterations):
				print(eliminationGenerator.next())
		elif choice == "5":
			eliminationGenerator.debug_generation()
		elif choice == "6":
			invDistGenerator = handleRecreationInvDistGenerator()
		elif choice == "7":
			eliminationGenerator = handleRecreationEliminationGenerator()
		elif choice == "8":
			break
		else:
			print("Invalid input. Please type in a number between 1 and 8, corresponding to what you want to do.")

	