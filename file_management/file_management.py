"""
File management
---------------
The goal of this exercise is to practice manipulating your file system:
creating folders and files, moving them around, and erasing them.

One piece of information to know about is that each python script contains its
own namespace. Such that, when in a script you define a = 1, a gets added to
the script namespace. But there are other variables that are added to that
namespace automatically: One example is __file__, which contains the filepath
to the current script.

1. Print the path to the current file/script and its containing folder.

2. In the same directory as this exercise, create a new directory called
`analysis`.

Hints: Why it isn't enough to just run:
>>> os.mkdir("analysis")
Where would that folder be? Build its absolute path to create it. Also note
that if the folder already exists, mkdir will raise an error if the folder
doesn't get removed before being created again. To remove a folder, compare the
following functions: `shutil.rmtree` and `os.rmdir`.

3. Create, wherever you are, a set of files with the names and content
described in the dictionary `contents` provided to you. Then, move all these
files into the `analysis` folder. For this, the `copy` function of the module
`shutil` will be useful.

4. Print the absolute path of all the Python `.py` files in this `analysis`
directory.

Hint: Using IPython's ? to remind yourself of what exactly os.path.splitext
returns.

Bonus
~~~~~
Turn your script into a function that takes an arbitrary directory path
and returns a list of Python files. Use it on the newly created analysis
folder.

Bonus Bonus
~~~~~~~~~~~
Let's do the same with a nice function of the os module: use os.walk to find
all Python files contained in all subdirectories of the folder containing this
current script. Again, test it on the analysis folder you created.
"""

import os
import shutil

contents = {
    'data.csv': 'Date,High,Low,Close\n'
                '4-Apr-2014,124,105,111\n'
                '5-Apr-2014,132,125,130\n'
                '6-Apr-2014,112,95,95\n'
                '7-Apr-2014,124,105,110\n',
    'script1.py': 'def bar(x):\n'
              '        print x\n',
    'script2.py': 'def foo(x):\n'
              '        print x*x\n',
    'readme.txt': 'This folder contains the data files scrapped off the web\n'
                  'from financial websites in csv formar as well as python\n'
                  'scripts for analyzing them.\n',
}


# your code goes here
#Q1
print 'The file is located at:', __file__
#Q2
container = os.path.dirname(__file__)
print 'the script is located in folder:', container

#Q3
target_folder = os.path.join(container, 'analysis')
if os.path.exists(target_folder):
    shutil.rmtree(target_folder)
os.mkdir(target_folder)

#Q4
for filename, content in contents.items():
    with open(filename, 'w') as f:
        f.write(content)

for filename in contents.keys():
    shutil.copy(filename, target_folder)
    os.remove(filename)
    
    
def search_python_file(folder):
    
    py = []
    for filename in os.listdir(folder):
        ext = os.path.splitext(filename)[1]
        if ext == '.py':
            py.append(os.path.abspath(os.path.join(folder, filename)))
    return py

print search_python_file(target_folder)
        