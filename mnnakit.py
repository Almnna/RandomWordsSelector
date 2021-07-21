import sys


class  CusExceptions(Exception):
  	class EmptyList(Exception):
  		"""docstring for EmptyList"""
  		def __init__(self, msg="Empty List"):
  			error = "{!@}-->> " + msg
  			super().__init__(error)
  			


def return_file_name(path):
	file_name = ""
	name = ""
	index = -1

	while True:
		name = path[index]
		if name == '\\' or name == '/':
			break;
		else:
			file_name += name;
			index -= 1;
	
	return file_name[::-1];

