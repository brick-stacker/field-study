# Water temperature reading (celcius)

measurements = [16.0,18.0, 19.0, 30.0]
def calculate_mean(values):
"""Retrun the arithmetic mean of an on-empty sequence of numbers"""
	return sum(values)/len(values)
print(f"Mean water temperature: {calculate_mean(measurements)} C")


