##Playtime with pip, virtualenv, different python versions.

###Documentation References
https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
https://pip.pypa.io/en/stable/user_guide/

###pip list and install
```
(env3) john@virtual-env-test:~/dimension-python$ pip list
pip (8.1.1)
pkg-resources (0.0.0)
setuptools (21.0.0)
wheel (0.29.0)
(env3) john@virtual-env-test:~/dimension-python$ pip install requests
Collecting requests
  Downloading requests-2.10.0-py2.py3-none-any.whl (506kB)
    100% |████████████████████████████████| 512kB 1.7MB/s 
Installing collected packages: requests
Successfully installed requests-2.10.0
(env3) john@virtual-env-test:~/dimension-python$ pip list
pip (8.1.1)
pkg-resources (0.0.0)
*requests (2.10.0)*
setuptools (21.0.0)
wheel (0.29.0)
```
###show available modules
```
>>> help('modules')

Please wait a moment while I gather a list of all available modules...

CDROM               antigravity         http                serializer
DLFCN               argparse            idlelib             setuptools
IN                  array               imaplib             shelve
TYPES               ast                 imghdr              shlex
...
```
###requirements.txt
####Generate requirements.txt:
```
(env3) john@virtual-env-test:~/dimension-python$ pip freeze > requirements.txt
(env3) john@virtual-env-test:~/dimension-python$ cat requirements.txt 
pkg-resources==0.0.0
requests==2.10.0
```
####Update environment with requirements.txt:
```
(env3) john@virtual-env-test:~/dimension-python$ pip install -r requirements.txt 
Requirement already satisfied (use --upgrade to upgrade): pkg-resources==0.0.0 in ./env3/lib/python3.5/site-packages (from -r requirements.txt (line 1))
Requirement already satisfied (use --upgrade to upgrade): requests==2.10.0 in ./env3/lib/python3.5/site-packages (from -r requirements.txt (line 2))
(env3) john@virtual-env-test:~/dimension-python$ 
```
###Virtualenv
Two environments, env=Python 2.7, env3=Python 3.51.  
Google code written in 2.7.  Dimension projects in 3.51.  
```
john@virtual-env-test:~/dimension-python$ . ./env3/bin/activate
(env3) john@virtual-env-test:~/dimension-python$ 
(env3) john@virtual-env-test:~/dimension-python$ 
(env3) john@virtual-env-test:~/dimension-python$ cd google-python-exercises/babynames/
(env3) john@virtual-env-test:~/dimension-python/google-python-exercises/babynames$ python babynames.py baby2000.html
  File "babynames.py", line 75
    print 'usage: [--summaryfile] file [file ...]'
                                                 ^
SyntaxError: Missing parentheses in call to 'print'
(env3) john@virtual-env-test:~/dimension-python/google-python-exercises/babynames$
(env3) john@virtual-env-test:~/dimension-python/google-python-exercises/babynames$ deactivate

john@virtual-env-test:~/dimension-python/google-python-exercises/babynames$ . ../env/bin/activate
(env) john@virtual-env-test:~/dimension-python/google-python-exercises/babynames$ python babynames.py baby2000.html | head
2000
Aaliyah 211
Aaron 41
Abagail 953
Abbey 425
Abbie 591
Abbigail 551
Abby 205
Abdullah 870
Abel 352
...
```

