# working with file parsing and sorting algorithms
# GOAL:
# read file and determine which interface has the lowest throughput associated with it.

import time

start = time.time()

# A little more complicated, but we could easily turn this into a function as well, and pass it any file
with open("example.csv", "r") as myfile:
	#print(myfile)
	innerstart = time.time()
	mylist = []	
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
				if mylist is empty and items[2] is an integer, 
				populate mylist with the interfaceID and throughput value from items
				(2nd and 3rd index respectively)
				
				Compare current value in items[2] with integer in mylist.
				If items[2] is lower, overwrite contents of mylist with 
				new interfaceID and throughput value
				"""
				if len(mylist) == 0 and isinstance(items[2], int):
					mylist.append((items[1],items[2]))

				elif len(mylist) != 0 and items[2] < mylist[0][1]:
					mylist[0] = (items[1],items[2])
			except Exception as err:
				print("Error: ",err)
			finally:
				print("what gets stored:",mylist)
	innerend = time.time()
	print("Inner time: ",innerend - innerstart)

end = time.time()
print("Inner time + file IO: ",end - start)
