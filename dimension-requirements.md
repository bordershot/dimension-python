##Python Basics:  
Understand python basics  
-COMPLETE - Understand ‘if, else if, else’ statements  
-COMPLETE - Understand ‘while’ and ‘for’ loops.  
-COMPLETE - LISTS – be able to create, modify, and retrieve a specific item in that LIST  
-COMPLETE - DICTIONARIES – be able to create, traverse, and retrieve a certain value from that key  
-FUNCTIONS  
  -COMPLETE - Write a simple python module that returns something, or can be just a simple print statement  
  -COMPLETE - Write a separate main script that imports that module and does something with it. (reuseSSH.py)  
  -COMPLETE - This will help John get familiar with functions  
  -COMPLETE - This will help john understand what ‘import’ really does (difference between ‘from XX import XX, import XX, import *’) (reuseSSH.py)  

##Python Environment:  
Packages  
-COMPLETE - How to install/remove packages with ‘pip’ (pip-packages-notes.md)  
-COMPLETE - Understand the usage of ‘requirements.txt’ (pip-packages-notes.md)  
-COMPLETE - List installed modules in that particular python environment (pip-packages-notes.md)  
-COMPLETE - Familiarize yourself with virtualenv and the benefits of it (pip-packages-notes.md)  

##Useful Modules:  
-COMPLETE - Get familiar with module ‘argparse’ (checkHost.py, movieLookup.py)  
  -COMPLETE - One of the arguments should be mandatory while another one is optional (checkHost.py, movieLookup.py)  
  -COMPLETE - If the number of arguments is incorrect, properly display the ‘help’ menu (checkHost.py, movieLookup.py)  
-COMPLETE - Get familiar with the ‘requests’ module. Write a script that performs http GET/POST requests. (movieLookup.py)  
-COMPLETE - Load JSON module and play around with how to parse JSON objects (movieLookup.py)  

##Projects:  
-COMPLETE - Write something in python that can ssh to a remote system, get data back (e.g. ls), and checks if something exists/matches (checkHost.py ssh's to remote host, runs dpkg -l, parses output to list, checks list for packages listed as command line args)  
  -COMPLETE(ISH) - In addition, write code that will catch an exception (e.g. if you can’t ssh into that box, inform the user with a simple ERROR message. (Didn't see an obvious way to catch ssh failing, but I did give an error message based on its return code.  I added a try/except block to movieLookup.py that works)  
-COMPLETE - (ADDED BY JOHN) Write demo of requests and json modules. (movieLookup.py)  

##Extra Credit:  
-Read over PEP8 and just familiarize yourself with a little of it.  
-COMPLETE - Run ‘pyflakes’ or ‘flake8’ against your code to see what it does and understand why it’s giving you errors (Issues created in github for pep8 and pyflakes)  
-COMPLETE(ISH) - Write unit tests for your scripts (test-checkHost.py, check that my regex parses dpkg -l output)  
-COMPLETE - I know John runs some trending graphs at home. Write python script(s) that will retrieve the metrics from his home devices and POST it to his trending backend. 
