# python-boilerplate

A boilerplate for creating command line tools in python.

Shows examples of:

* Required parameters
* Optional arguments
* Restricted Choices
* Running a subprocess
* Reading a configuration file

Examples:

```
z@zap:~/dev/python-boilerplate % ./boilerplate.py -h                                                                                                                                                                      (master*=)
usage: boilerplate.py [-h] [--foo [FOO]] [--bar BAR [BAR ...]]
                      [--subprocess [SUBPROCESS]]
                      {rock,paper,scissors} [parameter]

A foo that bars

positional arguments:
  {rock,paper,scissors}
                        A route to rock, paper or scissors
  parameter             A parameter

optional arguments:
  -h, --help            show this help message and exit
  --foo [FOO]           foo help
  --bar BAR [BAR ...]   bar help
  --subprocess [SUBPROCESS]
                        Run a subprocess

And that's how you'd foo a bar
```

```
z@zap:~/dev/python-boilerplate % ./boilerplate.py rock                                                                                                                                                                     (master=)
Namespace(bar=None, foo=None, parameter=None, routes='rock', subprocess=None)
True
```

```
z@zap:~/dev/python-boilerplate % ./boilerplate.py hand                                                                                                                                                                     (master=)
usage: boilerplate.py [-h] [--foo [FOO]] [--bar BAR [BAR ...]]
                      [--subprocess [SUBPROCESS]]
                      {rock,paper,scissors} [parameter]
boilerplate.py: error: argument routes: invalid choice: 'hand' (choose from 'rock', 'paper', 'scissors')
```

```
z@zap:~/dev/python-boilerplate % ./boilerplate.py rock --subprocess                                                                                                                                                       (master*=)
Namespace(bar=None, foo=None, parameter=None, routes='rock', subprocess=<function run_subprocess at 0x7f4da3154950>)
True
total 16
-rwxr-xr-x 1 z z 1304 Mar  6 20:19 boilerplate.py
-rw-r--r-- 1 z z   31 Mar  6 19:22 config.ini
-rw-r--r-- 1 z z 1068 Mar  6 20:11 LICENSE
-rw-r--r-- 1 z z 2325 Mar  6 20:20 README.md
```

```
z@zap:~/dev/python-boilerplate % ./boilerplate.py rock test --foo foo --bar bar1 bar2 bar3 --subprocess
Namespace(bar=['bar1', 'bar2', 'bar3'], foo='foo', parameter='test', routes='rock', subprocess=<function run_subprocess at 0x7fb30cbd9950>)
True
total 16
-rwxr-xr-x 1 z z 1261 Mar  6 20:04 boilerplate.py
-rw-r--r-- 1 z z   31 Mar  6 19:22 config.ini
-rw-r--r-- 1 z z 1068 Mar  6 20:11 LICENSE
-rw-r--r-- 1 z z  603 Mar  6 20:10 README.md

```

