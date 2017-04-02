# Purpose
Python implement trie data structure as practice.  

# References
## Trie Wikipedia
https://en.wikipedia.org/wiki/Trie

## Python html5lib/trie
https://github.com/html5lib/html5lib-python

# Results

## TODO:

### Populate trie
Read file numbers_test.txt line by line.  
For each line see if trie contains number.  
If trie doesn't contain number, insert number into trie.  

### Read from trie
Write a method to return list of numbers between a and b.
This may require depth first search, each node has a property visited of type bool.

#### Traverse tree
e.g. Visit "leftmost" nodes (e.g. child["0"]) as deep as possible, back up and mark child visited.
Then visit next child.

### Implement delete a number
Delete last node and any parents without children.

---

# data/input/numbers_test.txt
Contains an unsorted list of 9 digit numbers.
For example these could represent social security numbers.
Numbers don't contain separators like "-" or ".".

## how to run program
### cd <project root directory>  
e.g.  
cd pythonProjects/trie_me

### create and activate virtual environment (see appendix)

### call main
python3 -m main  
or  
python -m main


## Unit tests
To run tests, open terminal shell.  
cd to project directory. Run tests via python command or bash script.

### python command
This command lists and tests all modules

python3 -m unittest tests.test_trie tests.test_node


# Appendix Install virtual environment and requirements

## create and activate virtual environment
### create virtual environment
In project root directory  
python3 -m venv ./venv

#### anaconda
If using Anaconda, python3 -m venv ./venv may throw error  
Error: Command '['/Users/stevebaker/Documents/projects/pythonProjects/trie_me/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.  
http://stackoverflow.com/questions/41857088/new-python-3-6-venv-giving-error-on-macos  
http://stackoverflow.com/questions/41412876/how-do-you-activate-an-anaconda-environment-in-the-terminal-with-mac-os-x?noredirect=1&lq=1  

conda create -n trie_me python=3.6

### activate virtual environment
cd project root directory  
activate virtual environment
#### macOS
source venv/bin/activate
##### anaconda
source activate trie_me
(trie_me) should show at beginning of command prompt  

#### Windows
venv\Scripts\activate

venv should show at beginning of command prompt  

## install items in requirements file
with virtual environment active
pip3 install -r requirements.txt
