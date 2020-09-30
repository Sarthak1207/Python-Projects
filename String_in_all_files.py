import os

search_path = input("Please enter the path where files are kept : ")
if not (search_path.endswith("\\") or search_path.endswith('/')):
	search_path = search_path + "\\"	

seach_string = input("Enter the string you want to search for : ")
outputfile = search_path + seach_string + '.txt'
with open(outputfile,"w+") as output:
	for fname in os.listdir(path = search_path):
		fo = open(search_path + fname)
		if seach_string in fo.read():
			filename = search_path + fname
			fo.seek(0,0)
			for line in fo:
				if line.startswith(seach_string):
					output.write(fname)
					output.write("    ")
					output.write(line)
	fo.close()
	
input("Please enter to exit")
