# dimension-python

Google coursework:
https://developers.google.com/edu/python/

Descriptions for exercises:
https://developers.google.com/edu/python/exercises/basic
string1.py -- complete the string functions in string1.py, based on the material in the Python Strings section (additional exercises available in string2.py)
list1.py -- complete the list functions in list1.py, based on the material in the Python Lists and Python Sorting sections (additional exercises available in list2.py)
wordcount.py -- this larger, summary exercise in wordcount.py combines all the basic Python material in the above sections plus Python Dicts and Files (a second exercise is available in mimic.py)

https://developers.google.com/edu/python/exercises/baby-names
Part A -- In the babynames.py file, implement the extract_names(filename) function which takes the filename of a baby1990.html file and returns the data from the file as a single list -- the year string at the start of the list followed by the name-rank strings in alphabetical order. ['2006', 'Aaliyah 91', 'Abagail 895', 'Aaron 57', ...]. Modify main() so it calls your extract_names() function and prints what it returns (main already has the code for the command line argument parsing). 

Part B -- If the flag --summaryfile is present, do the following: for each input file 'foo.html', instead of printing to standard output, write a new file 'foo.html.summary' that contains the summary text for that file.

https://developers.google.com/edu/python/exercises/copy-special
The copyspecial.py program takes one or more directories as its arguments. We'll say that a "special" file is one where the name contains the pattern __w__ somewhere, where the w is one or more word chars.

Part A -- Gather a list of the absolute paths of the special files in all the directories.

Part B -- If the "--todir dir" option is present at the start of the command line, do not print anything and instead copy the files to the given directory, creating it if necessary. Use the python module "shutil" for file copying.

Part C -- If the "--tozip zipfile" option is present at the start of the command line, run this command: "zip -j zipfile <list all the files>". This will create a zipfile containing the files.

https://developers.google.com/edu/python/exercises/log-puzzle

An image of an animal has been broken it into many narrow vertical stripe images. The stripe images are on the internet somewhere, each with its own url. The urls are hidden in a web server log file. Your mission is to find the urls and download all image stripes to re-create the original image.

Part A -- Log File To Urls
Part B -- Download Images Puzzle
Part C -- Image Slice Descrambling
