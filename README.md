# Purpose
Python implement trie data structure as practice.  

# References
## Trie Wikipedia
https://en.wikipedia.org/wiki/Trie

## trie2.py
This module creates a trie of nested dictionaries.
http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python#11016430
http://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words#36977856

## Data Structures: Tries
java
https://youtu.be/zIjfhVPRZCg

## Data Structures: Solve 'Contacts' Using Tries
Java, shows recursive method with string argument
Was helpful for figuring out how to find next node
https://youtu.be/vlYZb68kAY0

## Python html5lib/trie
https://github.com/html5lib/html5lib-python

## TreeTraverser
Android app to traverse binary tree
https://github.com/beepscore/TreeTraverser

https://medium.com/algorithms/trie-prefix-tree-algorithm-ee7ab3fe3413
## Swift
### trie
https://github.com/raywenderlich/swift-algorithm-club/tree/master/Trie
### radix trie
https://github.com/raywenderlich/swift-algorithm-club/tree/master/Radix%20Tree

# Results

## trie.py
Creates a trie of Node objects.

### traversal methods
#### next_item
#### items
#### items_in_range
#### items_with_name

## trie2.py
This module creates a trie of nested dictionaries.
list_words works, but successor isn't working yet.


---

# data/input/numbers_names_test.txt
Contains an unsorted list of 9 digit numbers and names.

For example these could represent social security numbers.

Numbers don't contain separators like "-" or ".".

## how to run program

### cd <project root directory>
e.g.
    cd pythonProjects/trie_me

### create and activate virtual environment (see appendix)

### run file

    python3 -m trie


## Unit tests
To run tests, open terminal shell.
cd to project directory. Run tests via python command or bash script.

### python command
This command lists and tests all modules

    python3 -m unittest discover -s tests/

alternatively, can supply test module names as args

    python3 -m unittest tests.test_node tests.test_trie tests.test_trie2


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

    source deactivate trie_me

