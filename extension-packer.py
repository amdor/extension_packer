import os
import argparse


DEFAULT_USER_JS = """
// ==UserScript==
// @name         UserScript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Description here
// @author       John Doe
// @require      https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js
// @match        https://www.your.target.domain.com
// ==/UserScript==

(function() {
})();
"""

DEFAULT_USER_JS_FILE_NAME = "index.user.js"


def create_concat_file(userscript_file_name, js_files):
	"""
	Append all files' content to the userscript file
	:param userscript_file_name: the file to append to
	:param js_files: the files from which the content will be added
	:return:
	"""
	with open(userscript_file_name, 'rt') as us_file:
		us_file_content = us_file.readlines()
	with open(userscript_file_name, 'w') as us_file:
		us_file_end = us_file_content.pop()
		us_file.writelines(us_file_content)
		for js_file_name in js_files:
			with open(js_file_name) as js_file:
				print("Processing " + js_file_name)
				us_file.write("////" + os.path.basename(js_file_name).upper() + "\n")
				us_file.writelines(js_file.readlines())
				us_file.write("\n\n")
		us_file.write(us_file_end)


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


def create_initial_us_file():
	f = open(DEFAULT_USER_JS_FILE_NAME, 'x')
	f.write(DEFAULT_USER_JS)
	f.close()


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
	userscript_file_name = next((file for file in js_files if file.endswith('.user.js')), DEFAULT_USER_JS_FILE_NAME)
	if userscript_file_name not in js_files:
		create_initial_us_file()
	create_concat_file(userscript_file_name, js_files)


if __name__ == "__main__":
	main()
