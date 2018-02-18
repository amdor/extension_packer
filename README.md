# Extension packer
Created to make userscript development easier. Use multiple files when developing your userscript (e.g. TamperMonkey) then pack it in one userscript file.
# Usage
run
```shell
python extension-packer.py /path/to/git/extension_packer/example/
```
<br/>
* If no path is given, the current directory of the script will be used as root.<br/>
* Traverses recursively, looking for *.js files.<br/>
  * If there is a *.user.js file already, then it completes the contents with the those found in the *.js files. Else it creates a new index.user.js file as template.
