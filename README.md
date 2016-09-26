# PYFiles
A Python folder and file system creator.

- creates nested folders in a predifined order along with any files from the command line

###Example:
		
		python3 pyfi.py /this/file/path/and/file.txt
		
###Output:


		.this
		|__ file
		       |__ path
		       		|__ and
		       				|__
		              			file.txt
		
####If you want to chain multiple folders and files on a same level simply:


###Example
	python3 pyfi.py /folder1+folder2 /folder2/folder3 


###Output


		. __ folder1
		.|__ folder2
				|_ folder3