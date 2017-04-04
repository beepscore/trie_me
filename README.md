# Purpose
Python implement trie data structure as practice.  

# References
## Trie Wikipedia
https://en.wikipedia.org/wiki/Trie

## Python html5lib/trie
https://github.com/html5lib/html5lib-python

## TreeTraverser
Android app to traverse binary tree
https://github.com/beepscore/TreeTraverser

# Results

## TODO:

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


# Appendix virtual environment and requirements

## venv create and activate virtual environment

### create virtual environment
In project root directory  
python3 -m venv ./venv

### activate virtual environment
cd project root directory  
activate virtual environment

#### macOS

    source venv/bin/activate
    
#### Windows

    venv\Scripts\activate

venv should show at beginning of command prompt  

## install items in requirements file
with virtual environment active

    pip3 install -r requirements.txt

## Appendix Anaconda create and activate virtual environment

### create virtual environment
In project root directory  

If using Anaconda, python3 -m venv ./venv may throw error  

Error: Command '['/Users/stevebaker/Documents/projects/pythonProjects/trie_me/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.  
http://stackoverflow.com/questions/41857088/new-python-3-6-venv-giving-error-on-macos  
http://stackoverflow.com/questions/41412876/how-do-you-activate-an-anaconda-environment-in-the-terminal-with-mac-os-x?noredirect=1&lq=1  

So instead use anaconda command  

    conda create -n trie_me python=3.6

### activate virtual environment
cd project root directory  
activate virtual environment

#### macOS, linux

    source activate trie_me
    
(trie_me) should show at beginning of command prompt  

    source deactivate

