# dimension-python

Sample code for Dimension Data.

##dimension-requirements.md  
Checklist of topics and goals, with sections marked complete

##checkHost.py:  
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

##rest-json.py:  
Totally useless script against http://jsonplaceholder.typicode.com/.  Experiment with requests module, json module.
* Get  
* Put  
* Post  
* Create dictionary from JSON response  

##movieLookup.py:  
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

##reuseSSH.py  
Project: Reuse SSH to host, run command, parse output, return 5 largest log files  
* import function from checkHost.py  

##test-checkHost.py
Project: Write a unit test for a function
* import dpkg_parse function from checkHost.py and test

##dailySparkData.py
Project: Reimplement Graphite collector from BASH with curl to Python  
* logs in to voltstats.net, downloads data as csvs, converts to graphite, uploads  
* import upload_to_graphite function from graphiteclient.py
