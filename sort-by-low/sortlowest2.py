# working with file parsing
# GOAL:
# read file and determine which interface has the lowest throughput associated with it.

import time
import collections

start = time.time()

# A little more complicated, but we could easily turn this into a function as well, and pass it any file
with open("example.csv", "r") as myfile:
	#print(myfile)
	innerstart = time.time()
	mydeque = collections.deque()
	for line in myfile.readlines():
		entries = line.split() # split file by line
		if len(entries) != 0: # if not EOF, split line by comma
			items = entries[0].split(",")
			try:	# convert string in third index to integer
				items[2] = int(items[2])
			except Exception as err: # sloppy error catching
				print("Error: ",err)
			else:
				print("line items for this iteration:",items)
			try:	
				""" 
				if mydeque is not empty and items[2] is less than the value stored in mydeque, 
				prepend mydeque with the interfaceID and throughput value from items
				(index 1 and 2 of items, respectively)

				if mydeque is empty or items[2] is greater than what is already there, 
				append the values from items instead. 
				
				This should both populate the first valid entry
				AND 
				ensure that the lowest throughput value always exists index 0 of mydeque
				"""
				if isinstance(items[2],int):					
					if len(mydeque) != 0 and items[2] < mydeque[0][1]:
						mydeque.appendleft((items[1],items[2]))
					else:
						mydeque.append((items[1],items[2]))

			except Exception as err:
				print("Error: ",err)
			finally:
				print("what gets stored:",mydeque)
	innerend = time.time()
	print("Inner time: ",innerend - innerstart)

end = time.time()
print("Inner time + file IO: ",end - start)
