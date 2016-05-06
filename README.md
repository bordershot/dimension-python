# dimension-python

Sample code for Dimension Data.

#checkHost.py:  
Project: SSH to host, run command, parse output  
* Error handling (not try-exception block, just ouput ssh error)
  * Script continues to try aditional hosts when a host isn't found.
* if/else
* for
* Lists
* functions
* argparse:
  * Required and optional arguments.
  * Display usage on error input.

#rest-json.py:  
Totally useless script against http://jsonplaceholder.typicode.com/.  Experiment with requests module, json module.
* Get  
* Put  
* Post  
* Create dictionary from JSON response  

#movieLookup.py:  
Project: Get familiar with JSON, requests, argparse modules  
* Error handling -- try/expect for url connection  
* if/else  
* for  
* while  
* Lists  
* Dictionary  
* argparse:  
    * Required and optional arguments.  
    * Display usage on error input.  
* requests:  
    * Only get, put/post not supported on API  
* json:  
    * Use json.loads to convert json to Dictionary  
    * Search returns multiple movies, so Dictionary contains a list of dictionaries per movie  

Sample usage:  
    ./movieLookup.py "Splash"  
    ./movieLookup.py "Star Wars" -s  

