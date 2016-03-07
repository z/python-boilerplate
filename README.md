# python-boilerplate

A boilerplate for creating command line tools in python.

Shows examples of:

* Positional arguments
* Optional arguments
* Restricted Choices
* Subparsers
* Running a subprocess
* Reading a configuration file

Examples:

```
z@zap:~/dev/python-boilerplate % ./boilerplate.py -h                                                                                                                                                                      (master*=)
usage: boilerplate.py [-h] [--foo [FOO]] [--bar BAR [BAR ...]]
                      [--subprocess [SUBPROCESS]]
                      {route1,route2} ... [parameter]

A foo that bars

positional arguments:
  {route1,route2}       sub-command help
    route1              route1 help
    route2              route2 help
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
z@zap:~/dev/python-boilerplate % ./boilerplate.py route1                                                                                                                                                                  (master*=)
Namespace(bar=None, baz=None, foo=None, parameter=None, route='route1', subprocess=None)
True
```

```
z@zap:~/dev/python-boilerplate % ./boilerplate.py route3                                                                                                                                                                  (master*=)
usage: boilerplate.py [-h] [--foo [FOO]] [--bar BAR [BAR ...]]
                      [--subprocess [SUBPROCESS]]
                      {route1,route2} ... [parameter]
boilerplate.py: error: argument route: invalid choice: 'route3' (choose from 'route1', 'route2')
```

```
./boilerplate.py --subprocess 1 route1
Namespace(bar=None, baz=None, foo=None, parameter=None, route='route1', subprocess='1')
True
total 16
-rwxr-xr-x 1 z z 1749 Mar  6 21:08 boilerplate.py
-rw-r--r-- 1 z z   31 Mar  6 19:22 config.ini
-rw-r--r-- 1 z z 1068 Mar  6 20:11 LICENSE
-rw-r--r-- 1 z z 2663 Mar  6 21:09 README.md
```

```
z@zap:~/dev/python-boilerplate %                                                                                                                                                                                          (master*=)
./boilerplate.py route1 --help           
usage: boilerplate.py route1 [-h] [--baz [BAZ]] [bar]

positional arguments:
  bar          bar help

optional arguments:
  -h, --help   show this help message and exit
  --baz [BAZ]  bar help
```

```
z@zap:~/dev/python-boilerplate %                                                                                                                                                                                          (master*=)
./boilerplate.py --subprocess 1 route1 --baz 10
Namespace(bar=None, baz='10', foo=None, parameter=None, route='route1', subprocess='1')
True
total 16
-rwxr-xr-x 1 z z 1749 Mar  6 21:08 boilerplate.py
-rw-r--r-- 1 z z   31 Mar  6 19:22 config.ini
-rw-r--r-- 1 z z 1068 Mar  6 20:11 LICENSE
-rw-r--r-- 1 z z 2663 Mar  6 21:09 README.md

```

