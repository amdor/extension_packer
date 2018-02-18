# Extension packer
Created to make userscript development easier. Use multiple files when developing your userscript (e.g. TamperMonkey) then pack it in one userscript file.
# Usage
run
```shell
python extension-packer.py /path/to/git/extension_packer/example/
```
output:
```
Path read from argument:  /home/zsolt/git/extension_packer/example/
JS file found: 3.js
JS file found: 2.js
JS file found: 1.js
Processing /home/zsolt/git/extension_packer/example/1.js
Processing /home/zsolt/git/extension_packer/example/sub1/2.js
Processing /home/zsolt/git/extension_packer/example/sub1/sub2/3.js
```
<br/>
If no path is given, the current directory of the script will be used as root.<br/>
Traverses recursively, looking for *.js files.<br/>
If there is a *.user.js file already, then it appends the contents with the *.js files. Else it creates a new index.user.js file.
