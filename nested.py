import sys
import os


def write_to_file(file_and_path, contents):
	with open(file_and_path, 'w') as file:
		file.write(contents)
	file.close()