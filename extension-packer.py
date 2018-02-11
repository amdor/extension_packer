import os
import argparse


def gather_extension_files(root):
	"""
	Traverses through all subdirectories of root collecting *.js filenames. Recursive.
	:param root: the basepoint of search
	:rtype: set
	:return: all found js filenames
	"""
	extension_files = set()
	for child in os.listdir(root):
		abs_path = os.path.join(root, child)
		if os.path.isdir(abs_path):
			extension_files |= gather_extension_files(abs_path)
		elif child.endswith(".js"):
			extension_files.add(abs_path)
			print("JS file found: " + child)
	return extension_files


def get_extension_path():
	"""
	Reads the command line arguments provided, or defaults to current path if no or not valid path is given
	:return: the directory path to traverse
	"""
	path = ""
	if not path:
		parser = argparse.ArgumentParser(description='Provide directory name to traverse')
		parser.add_argument('extension_path', nargs='?', metavar='path')
		namespace = parser.parse_args()
		if os.path.isdir(namespace.extension_path.strip()):
			path = namespace.extension_path
			print("Path read from argument: ", path)

	if not path:
		path = os.path.dirname(os.path.realpath(__file__))
		print("Default working path: ", path)
	return path


def main():
	path = get_extension_path()
	js_files = gather_extension_files(path)



if __name__ == "__main__":
	main()
