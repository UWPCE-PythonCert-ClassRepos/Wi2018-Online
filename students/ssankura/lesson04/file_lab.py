
def printfilenames():
	import os
	arr = os.listdir()
	print("List of files in current directory: ")
	for file in arr:
		print (os.path.abspath(file))

def copyfile():
	chunksize = 1024 
	
	sourcefilename = input("Enter Source File Name > ")
	srcfileext = sourcefilename[-4:]
	
	outputfilename = input("Enter Target File name without file extension > ")
	targetfilename = outputfilename + srcfileext


	srcfile = open(sourcefilename, 'rb')
	destfile = open(targetfilename,'wb')
	
	bytes_read = srcfile.read(chunksize)
	while (bytes_read):
		destfile.write(bytes_read)
		bytes_read = srcfile.read(chunksize)
	
	destfile.close()
	srcfile.close()

if __name__ == "__main__":
	printfilenames()
	copyfile()
