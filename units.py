import sys
import copy

def sort(units, relations, n):
	
	sorted = ""
	data = dict()
	for i in range(n-1):
		data[i] = relations[i].split()
	
	# Succesfully broken down all units to elements in a list, next step is to calculate how all units relate to each other
	# Return all units sorted in correct order, represented in a string
	return sorted

def main():
	
	while(1):
		# Read input
		n = int(sys.stdin.readline())
		if n == 0:
			break
		count = 0
		units = sys.stdin.readline().split()
		
		relations = {}
		for i in range(n-1):
			relations[i] = sys.stdin.readline().rstrip()
		
		res = dict()
		# The chunk of units is return as a string and stored in a result dictionary.
		res[count] = sort(units, relations, n)
		count += 1
		# Continue to next chunk of units...
			
		
if __name__ == '__main__':
	main()