# Purpose
Python implement trie data structure as practice.  

# References
## Python html5lib/trie
https://github.com/html5lib/html5lib-python

# Results

## how to run program
### cd <project root directory>  
e.g.  
cd pythonProjects/trie_me

### acitvate virtual environment  

### call main
python3 -m main  
or  
python -m main


## Unit tests
To run tests, open terminal shell.  
cd to project directory. Run tests via python command or bash script.

### python command
This command lists and tests all modules

python3 -m unittest tests.test_trie


# Appendix Install virtual environment and requirements

## create virtual environment
In project root directory  
python3 -m venv ./venv

## activate virtual environment
cd project root directory  
activate virtual environment
### macOS
source venv/bin/activate
### Windows
venv\Scripts\activate

venv should show at beginning of command prompt  

## install items in requirements file
with virtual environment active
pip3 install -r requirements.txt
