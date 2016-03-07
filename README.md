# python-boilerplate

A boilerplate for creating command line tools in python.

Shows examples of:

* Required parameters
* Optional arguments
* Restricted Choices
* Running a subprocess
* Reading a configuration file

`./boilerplate.py rock test --foo foo --bar bar1 bar2 bar3 --subprocess`

Returns:

```
z@mint:~/dev/python-boilerplate % ./boilerplate.py rock test --foo foo --bar bar1 bar2 bar3 --subprocess
Namespace(bar=['bar1', 'bar2', 'bar3'], foo='foo', parameter='test', routes='rock', subprocess=<function run_subprocess at 0x7fb30cbd9950>)
True
total 16
-rwxr-xr-x 1 z z 1261 Mar  6 20:04 boilerplate.py
-rw-r--r-- 1 z z   31 Mar  6 19:22 config.ini
-rw-r--r-- 1 z z 1068 Mar  6 20:11 LICENSE
-rw-r--r-- 1 z z  603 Mar  6 20:10 README.md

```