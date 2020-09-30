import os

search_path = input("Please enter the path where files are kept : ")
if not (search_path.endswith("\\") or search_path.endswith('/')):
	search_path = search_path + "\\"	

seach_string = input("Enter the string you want to search for : ")
	
for fname in os.listdir(path = search_path):
	fo = open(search_path + fname)
	if seach_string in fo.read():
		print(fname)
	fo.close()
