from random import randint
import timeit
import numpy as np
import matplotlib.pyplot as plt
import math


def main():
	data = generateData(2500)
	
	dataSelectionSort = data.copy()
	selectionSort(dataSelectionSort, "method1")
	#plotData(sortedData)

	dataSelectionSort2 = data.copy()
	selectionSort(dataSelectionSort2, "method2")
	# #plotData(sortedData)

	dataBubbleSort = data.copy()
	bubbleSort(dataBubbleSort)
	# #plotData(sortedData)

	dataInsertionSort = data.copy()
	insertionSort(data)

	dataMergeSort = data.copy()
	start = timeit.default_timer()
	mergeSort(dataMergeSort)
	stop = timeit.default_timer()
	print(f"\tMerge Sort took {(stop - start)*1000000} microseconds to execute!")

	dataQuickSort = data.copy()
	#dataQuickSort = [7,8,7,4,10,3,5]
	start = timeit.default_timer()
	result = quickSort(dataQuickSort, [])
	stop = timeit.default_timer()
	#print(f"Result from QuickSort = {result}")
	print(f"\tQuick Sort took {(stop - start)*1000000} microseconds to execute!")
	
def generateData(amount):
	data = []
	for i in range(0, amount):
		data.append(randint(0, 100))
	return data

def selectionSort(data, methodname):
	#print(f"Data is {data}")
	if methodname == "method1":
		start = timeit.default_timer()

		sortedList = []
		for i in range(0, len(data)):
			lowestValue = min(data)
			sortedList.append(min(data))
			data.remove(min(data))
			#print(f"sortedList is now {sortedList}")
			#print(f"sortedList is now {sortedList}")
		stop = timeit.default_timer()
		#print(f"\tsortedList = {sortedList}") 
		print(f"\tSelection Sort {methodname} took {(stop - start)*1000000} microseconds to execute!")

	if methodname == "method2":
		start = timeit.default_timer()

		for i in range(len(data)):
			# print(i)
			min_idx = i 
			# print(f"Analyzing index {i}")
			for j in range(i+1, len(data)):
				# print(f"If {sortedList[min_idx]} greater than {sortedList[j]}")
				if data[min_idx] > data[j]:
					# print(f"Index {j} becomes the new minimum index")
					min_idx = j     
			data[i], data[min_idx] = data[min_idx], data[i] 
			# print(f"Swapped minimum index to front: {sortedList}")
		stop = timeit.default_timer()
		#print(f"\tsortedList = {data}")
		print(f"\tSelection Sort {methodname} took {(stop - start)*1000000} microseconds to execute!")

def bubbleSort(data):
	#print(f"Data is {data}")
	# stateArray = []

	start = timeit.default_timer()

	swapHappened = True
	while swapHappened:
		swapHappened = False
		#stateArray.append(data)
		for i in range(0, len(data) - 1):
			if data[i] > data[i + 1]:
				data[i], data[i + 1] = data[i + 1], data[i]
				swapHappened = True
		#stateArray.append(data)
	stop = timeit.default_timer()
	#print(f"sortedList is {data}")
	print(f"\tBubble Sort took {(stop - start)*1000000} microseconds to execute!")


def insertionSort(data):
	#print(f"Data is {data}")
	start = timeit.default_timer()

	sortedList = [data[0]]
	unsortedList = data[1:]

	while len(unsortedList) > 0:
		sortedList = swapUnsorted(unsortedList[0], sortedList)
		unsortedList.pop(0)

	stop = timeit.default_timer()
	#print(f"\tsortedList is {sortedList}")
	print(f"\tInsertion Sort took {(stop - start)*1000000} microseconds to execute!")

def swapUnsorted(element, sortedList):
	sortedList.append(element)
	index = len(sortedList) - 1	

	for i in range(0, len(sortedList) - 1):
		if sortedList[index] < sortedList[index - 1]:
			# print(f"element at {sortedList[index]} < {sortedList[index - 1]}, swapping")
			# print(f"sortedList before {sortedList}")
			sortedList[index - 1], sortedList[index] = sortedList[index], sortedList[index - 1]
			# print(f"sortedList after {sortedList}")
			index -= 1
		else:
			break
	return sortedList

#################### MERGE SORT ######################################
def mergeSort(data):
	#print(f"data is now {data}")

	if len(data) <= 1:
		return data

	divide1 = mergeSort(data[0: math.ceil(len(data) / 2)])
	divide2 = mergeSort(data[math.ceil(len(data) / 2):])
	counter = 0

	while len(divide1) != 0 and len(divide2) != 0:
		# print(f"\tChecking if first element div1, {divide1[0]}, is smaller than div2, {divide2[0]}")
		if divide1[0] < divide2[0]:
			# print(f"\tIt is, so the first element of div1 gets popped and added to data")
			data[counter] = divide1.pop(0)
			# print(f"\t\tWhich makes data now {data}")
		else:
			# print(f"\tIt is not, so the first element of div2 gets popped and added to data")
			data[counter] = divide2.pop(0)
			# print(f"\t\tWhich makes data now {data}")

		counter += 1
	sortedList = data[:-len(divide1 + divide2)] + divide1 + divide2
	#print(f"Mergesort result is {sortedList}")
	return sortedList


#################### ########### ######################################

#################### QUICK SORT ######################################
# def quickSort(data, low, high):
# 	print(f"Data is {data}")
# 	#print(f"low is {low}")
# 	if low < high:
# 		partition = partitionData(data, low, high)
# 		quickSort(data, low, partition - 1)
# 		quickSort(data, partition + 1, high)
# 	print(f"QuickSort result is {data}")

# def partitionData(array, low, high):
# 	pivot = array[high]
# 	#print(f"pivot is {pivot}")
# 	index = low - 1

# 	for j in range(low, high - 1):
# 		if array[j] <= pivot:
# 			index += 1
# 			array[index], array[j] = array[j], array[index]
# 	array[index + 1], array[high] = array[high], array[index + 1]
# 	return index + 1

# def quickSort(data): # According to Youtuber, wrong though!
# 	print(f"Data is {data}")

# 	wall_index = 0
	
# 	while(wall_index < len(data)):
		
# 		print(f"Wall index is {wall_index}")
# 		current_element = data[wall_index]
# 		print(f"Current element is {current_element}")
# 		pivot_index = len(data) - 1
# 		print(f"Pivot index is {pivot_index}")
# 		pivot = data[pivot_index]
# 		print(f"Pivot is {pivot}")

# 		for i in range(wall_index, pivot_index):
# 			print(f"current element to analyse is {data[i]}")
# 			if data[i] < pivot:
# 				print(f"\tcurrent element {data[i]} is smaller than pivot {pivot}! Data before swapping = {data}")
# 				data[wall_index], data[i] = data[i], data[wall_index]
# 				print(f"\tData after swapping = {data}")
# 				wall_index += 1
		
# 		print(f"Wall index to put back into is {wall_index} which is element {data[wall_index]}")
# 		data[pivot_index], data[wall_index] = data[wall_index], data[pivot_index] # Swap pivot with wall position
# 		print(f"Data after putting the pivot back on the wall = {data}")
# 		wall_index += 1

# 	print(f"QuickSort result is {data}")

def quickSort(data, result):
	#print(f"Data is now {data}")
	if len(data) <= 1:
		# print(f"\treturning data {data} now")
		# print(f"result is {result} so far")
		if data != []:
			result.append(data[0])
		return data

	# pick a pivot	
	pivot = data[len(data) - 1]
	smallerthan = []
	biggerthan = []

	for element in data[0: -1]:
		if element <= pivot:
			smallerthan.append(element)
		else:
			biggerthan.append(element)

	# print(f"\tsmallerthan is {smallerthan}")
	# print(f"\tbiggerthan is {biggerthan}")

	smallerthan = quickSort(smallerthan, result)
	result.append(pivot)
	biggerthan = quickSort(biggerthan, result)

	return result

#################### ########### ######################################


def plotData(data):
	bars = []
	for i in range(len(data)):
		bars.append(i)
	y_pos = np.arange(len(bars))

	# Create bars
	plt.bar(y_pos, data)
	# Create names on the x-axis
	plt.xticks(y_pos, bars)
	 
	# Show graphic
	plt.show()


if __name__ == '__main__':
	main()