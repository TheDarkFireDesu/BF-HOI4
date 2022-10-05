import os

ddslist = []
exceptionlist = []
ddsdict = {}
inputpath = ""

def main():
	dirName = input("Please Input a Path to the File Directory:\n")
	print(f'Creating batch script for directory {dirName}')

	getfiles(dirName)

	outScript = open('convertDDS.nvtt', 'w') # Start a new script

	for file in ddsdict:
		newFileName = file.rpartition('.')[0] + '.dds' # Replace .png with .dds
		outScript.write(f'\"{file}\" --no-mips --format bc1 --output \"{newFileName}\"\n')

	outScript.close()
	print('Done')


def getfiles(path):
	for filename in os.listdir(path):
		f = os.path.join(path,filename)
		if os.path.isfile(f):
			if '.dds' in f:
				ddsdict[f] = filename
				ddslist.append(filename)
		else:
			getfiles(f)

if __name__ == "__main__":
	main()